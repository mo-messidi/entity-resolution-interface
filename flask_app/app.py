from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from google_query import analyze

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    first_name = StringField('First Name:')
    last_name = StringField('Last Name:')
    organization = StringField('Organization:')
    location = StringField('Location:')
    tld = StringField('TLD:')
    num_query = StringField('Number of Query:')
    stop_query = StringField('Stop Query:')
    pause_time = StringField('Pause Time:')
    extra_filter = StringField('Extra filters:')
    to_file = StringField('File Path:')


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        organization = request.form['organization']
        location = request.form['location']
        tld = request.form['tld']
        num_query = request.form['num_query']
        stop_query = request.form['stop_query']
        pause_time = request.form['pause_time']
        extra_filter = request.form['extra_filter']
        to_file = request.form['to_file']
        input = {}
        input['first_name'] = first_name
        input['last_name'] = last_name
        input['organization'] = organization
        input['location'] = location
        input['tld'] = tld
        input['num_query'] = num_query
        input['stop_query'] = stop_query
        input['pause_time'] = pause_time
        input['extra_filter'] = extra_filter
        input['to_file'] = to_file
        if (analyze(input) == 1):
            flash('Operation successfully.')
        else:
            flash('Something went wrong. Please check the console logs.')
    return render_template('hello.html', form=form)


if __name__ == "__main__":
    app.run()
