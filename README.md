# MSTAR FLASK DEMO ON HEROKU
---
This is a list of things I did to get this repo up and running. The current version of the app is located at
[https://flask-demo-mstar.herokuapp.com/](https://flask-demo-mstar.herokuapp.com/)
---
# Create a  project
`mkdir heroku-flask-demo`
`cd heroku-flask-demo`
`git init`
`heroku apps:create flask-demo-mstar --buildpack heroku/python`
`heroku addons:add heroku-postgresql:hobby-dev`

### Create config.py
```
import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```
### Create demo.py
```
from app import create_app

app = create_app()
```
### Create app/\__init\__.py
```
from config import Config

def create_app(config_class=Config):
    print("creating")
```
### Check it works
virtualenv --python python3 env
source env/bin/activate
python demo.py
```
(env) user@computer:~/hub/heroku-flask-demo$ python demo.py
creating
```

## Create a example page

`pip install Flask`
### Update app/__init__.py
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
### update demo.py
```
from app import create_app

app = create_app()
# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
```

 ## Run
 ` demo.py `
Will run up the app on port 8080

## For completelness, create .gitignore
```
*.py[cod]
env
__pycache__
```

# To run on heroku
Add gunicorn
``pip insall gunicorn``
and create requirements.txt
``pip freeze > requirements.txt``

add a runtime.txt
```
python-3.7.0
```

and procfile
``web: gunicorn demo``


and then run locally
``heroku local web``




---
**Here is a demo**
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku
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
