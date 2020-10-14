# Sennder Movie App

I am used to the Python language but I never used the Django framework before this project.
This project took me 2.5 hours to complete.
In order to facilitate reading of the `diff`, I divided my work into 4 commits:
- Analysis of the project
- Coding
- Caching
- Testing

You will find all relevant code under the `app/movies` folder.

## Installation steps

1) Install Python3

2) Install Django

```
python3 -m pip install Django
```

3) Install dependencies

```
pip3 install requests
```

## How to run

1) The `app` folder contains the application. Move into it: `cd app`

2) Run the development server: `python3 manage.py runserver`

3) Go to http://127.0.0.1:8000/movies/

## How to test

Run: `python3 manage.py test`

## Check PEP8 compliance

Install: `pip3 install pycodestyle`

Run: `pycodestyle movies`
