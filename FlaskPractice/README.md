# Requirement
![](https://img.shields.io/badge/Flask-1.0.2-green.svg?longCache=true&style=for-the-badge)
![](https://img.shields.io/badge/WTForms-2.2.1-green.svg?longCache=true&style=for-the-badge)
![](https://img.shields.io/badge/gunicorn-19.9.0-green.svg?longCache=true&style=for-the-badge)
![](https://img.shields.io/badge/beautifulsoup4-4.6.3-green.svg?longCache=true&style=for-the-badge)

macOS<br>
Python 3.7 (or above)<br>
Brew<br>
Git<br>
HeroKu Acount<br>
**IMPORTANT : Extremely Ultra Super fast Internet Connection**<br>

# Local Deploy
After clone repo, simply run `InstallModule.py`<br>
Or run these script in terminal.
```
pip install flask
pip install flask-wtf
pip install flask gunicorn
pip install beautifulsoup4
pip install lxml
pip install html5lib
pip install requests
```

Run
```
python app.py
```

# Deploy to HeroKu
Install Heroku CLI first
```
brew install heroku
```

Then Login to HeroKu Account
```
heroku login
```

Move to Working Dir
```
cd some/where/FlaskPractice
```

List all module used in project
```
python -m pip freeze > requirements.txt
```

Create a file called `Procfile`, then add below text.
```
web: gunicorn app:app
```

Init git and connect repo on Heroku
```
git init
heroku git:remote -a heroku_app_name
```

Push To HeroKu and run
```
git add .
git commit -am 'Something just did'
git push heroku master
cat Procfile
```


[Deploying Flask to Heroku](https://www.youtube.com/watch?v=pmRT8QQLIqk)