from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Stupid:
from django.db import connection
from django.contrib.auth.models import User

# Create your views here.

# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             login(request, form.save())
#             return redirect("posts:list")
#     else:
#         form = UserCreationForm()
#     return render(request, "users/register.html", { "form": form })

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        sql = f"""
        INSERT INTO auth_user (
            username, password, email, first_name, last_name, is_staff, is_active, is_superuser, date_joined
        ) VALUES (
            '{username}', '{password}', '', '', '', 0, 1, 0, '1988-01-01'
        )
        """
        with connection.cursor() as c:
            c.execute(sql)

        user = User.objects.get(username=username)
        login(request, user)
        return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })

# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         user = form.get_user()
        
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect("posts:list")
#     else:
#         form = AuthenticationForm()
#     return render(request, "users/login.html", { "form": form })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        sql = f"SELECT * FROM auth_user WHERE username = '{username}' AND password = '{password}'"

        with connection.cursor() as c:
            c.execute(sql)
            user = c.fetchone()
        if user:
            user_object = User.objects.get(pk=user[0])
            login(request, user_object)
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
