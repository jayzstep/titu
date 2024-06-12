### clone repository
```bash
git clone https://github.com/jayzstep/titu.git
```

### create virtual environment

```bash
python -m venv venv
venv/bin/activate
```

### install dependencies
You should have everything you need if you've done the part 2 of the course.

```bash
pip install -r requirements.txt
```

### setup database

```bash
python3 manage.py migrate
```

### run server
```bash
python3 manage.py runserver
```

follow the instructions on screen. There should be a server running at `http://127.0.0.1:8000/`




