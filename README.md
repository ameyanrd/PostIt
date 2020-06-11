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
3. Install Django with pip
`python -m pip install Django`

4. Open the PostIt folder and migrate all files
```
python manage.py makemirations
python manage.py migrate
```

5. Run the server
```python manage.py runserver```

6. Start the app at [http://127.0.0.1:8000](http://127.0.0.1:8000)

7. Alternatively, to use Gunicorn, run the following commands:
```
python -m pip install gunicorn
pip install dj-static
gunicorn PostIt.wsgi
```
