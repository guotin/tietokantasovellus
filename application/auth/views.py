from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import Account
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = Account.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               errorMessage = "Login failed, check input or register")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods=["GET","POST"])
def auth_register():

    if request.method == "GET":
        return render_template("auth/new.html", form = RegisterForm())

    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("auth/new.html", form = form)

    newUser = Account.query.filter_by(username=form.username.data).first()
    
    if newUser:
        return render_template("auth/new.html", form=form, errorMessage = "Username already taken")

    newUser = Account(form.username.data, form.password.data)
    db.session().add(newUser)
    db.session.commit()

    login_user(newUser)

    return redirect(url_for("index"))

@app.route("/auth", methods=["GET"])
def auth_index():
    return render_template("auth/list.html", users=Account.find_users_with_most_reviews())

    


    
