from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


app = Flask(__name__)

app.secret_key = "your_mom"

bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8)])
    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.email.data == "admin@email.com" and form.password.data == "12345678":
                return render_template('success.html')
            else:
                return render_template("denied.html")
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
