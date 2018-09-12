# Requirement
macOS<br>
Python 3.7 (or above)<br>
Brew<br>
Git<br>
HeroKu Acount<br>
**IMPORTANT : Extremely Ultra Super fast Internet Connection**<br>

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
cat cat Procfile
```


[Deploying Flask to Heroku](https://www.youtube.com/watch?v=pmRT8QQLIqk)