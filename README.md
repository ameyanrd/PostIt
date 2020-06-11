# PostIt
An online platform to showcase your ideas.

## Installation Setup:
1. Clone the repository.<br/>
`git clone https://github.com/ameyanrd/PostIt`
2. Setup your virtual environment and activate it.
```
python3 -m venv ~/.virtualenvs/postit
source ~/.virtualenvs/postit/bin/activate
```
3. Install Django with pip<br/>
`python -m pip install Django`

4. Open the PostIt folder and migrate all files
```
python manage.py makemigrations blog
python manage.py migrate
```

5. Install the third-party app dj-static to load static files. (Required by Gunicorn). Note that this step is required for running step 6 as well.<br/>
`pip install dj-static`

6. Run the server<br/>
`python manage.py runserver`

7. Start the app at [http://127.0.0.1:8000](http://127.0.0.1:8000)

8. Alternatively, to use Gunicorn, run the following commands:
```
python -m pip install gunicorn
gunicorn PostIt.wsgi
```
