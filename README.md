# demo [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku]
git clone https://github.com/miguelgrinberg/microblog
cd microblog/
git checkout v0.18
heroku apps:create flask-microblog-mstar
git remote -v
heroku addons:add heroku-postgresql:hobby-dev
heroku config:set LOG_TO_STDOUT=1
heroku config:set FLASK_APP=microblog.py
git checkout -b deploy
git push heroku deploy:master
heroku open


# do something locally
virtualenv --python python3 env
source env/bin/activate
python main.py
heroku local web

# set/install requirements
pip freeze > requirements.txt
pip install -r requirements.txt




### THIS PROJECT
mkdir heroku-flask-demo
cd heroku-flask-demo
git init
heroku apps:create flask-demo-mstar
heroku addons:add heroku-postgresql:hobby-dev

- Create config.py
```
import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```
- Create demo.py
```
from app import create_app

app = create_app()

```
- Create app/__init__.py
```
from config import Config

def create_app(config_class=Config):
    print("creating")

```
--Check it works
virtualenv --python python3 env
source env/bin/activate
python demo.py
```
(env) mstar@s168366:~/hub/heroku-flask-demo$ python demo.py
creating
```

- create a example page
pip install Flask
pip freeze > requirements.txt
Update app/__init__.py
```
from config import Config
from flask import Flask


def create_app(config_class=Config):
    app = Flask(__name__)
    print("creating")

    @app.route('/')
    def hello():
        return "Hello World!"

    return app
```
and
demo.py
```
from app import create_app

app = create_app()
# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
```
Create .gitignore
```
*.py[cod]
env
__pycache__
```
