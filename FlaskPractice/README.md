# Requirement
macOS
Python 3.7 (or above)
Brew
Git
HeroKu Acount
**IMPORTANT : Extremely Ultra Super fast Internet Connection**

# Local Deploy
After clone repo, run these script in terminal.
```
pip install flask
pip install flask-wtf
pip install flask gunicorn
```

Run
```
python main.py
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

List all module used in project
```
python -m pip freeze > requirements.txt
```

Move to Working Dir and init git
```
cd some/where/FlaskPractice
git init
```

Connect Repo on Heroku
```
heroku git:remote -a heroku_app_name
```

Push To HeroKu and run
```
git add .
git commit -am 'Something just did'
git push heroku master
cat cat Procfile
```


[Deploying Flask to Heroku](https://www.youtube.com/watch?v=pmRT8QQLIqk)