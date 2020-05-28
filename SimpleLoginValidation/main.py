from flask import Flask, render_template, url_for, flash, request, redirect
from loginModel import LoginForm
from google.cloud import datastore

# TODO Server to Server Authentications
# https://cloud.google.com/docs/authentication/production?hl=zh-tw#windows

# App Start
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a83c51c8b7fc804eb395d7c1d753fa28'


# Index
@app.route('/', methods=['GET', 'POST'])
def hello():
    form = LoginForm()

    email = form.email.data
    password = form.password.data

    if request.method == 'GET':
        return render_template('index.html', form=form, post=False)
    elif request.method == 'POST':
        client = datastore.Client()
        #　Method: query it
        query = client.query(kind='account')
        query = query.add_filter('EmailAddress', '=', email)
        query = query.add_filter('Password', '=', password)
        result = query.fetch()
        # <Entity('account', 5643280054222848) {'Password': 'password', 'FirstName': 'John', 'EmailAddress': 'john@gmail.com'}>
        resultLists = list(result)

        if len(resultLists) == 0:
            return render_template('index.html', form=form, post=True)
        else:
            global firstName
            for key, value in resultLists[0].items():
                if key == 'FirstName':
                    firstName = value
            return render_template('index.html', form=form, post=True, accountName=firstName)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
    # app.run(debug=True)
