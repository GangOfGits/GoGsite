from notjoshno import app
from flask import render_template, redirect, session, request, url_for, abort
from notjoshno.authentication import verify_password
from notjoshno.web_pages import web_page

web_pages = {}
web_pages["main"] = web_page("main.html", "Home")
web_pages["namegenerator"] = web_page("namegenerator.html", "Name Generator")
web_pages["login"] = web_page("login.html", "Login")
web_pages["main"] = web_page("main.html", "Home")

@app.route("/")
def home():
    return web_pages["main"].render()


@app.route("/app/<string:application_name>")
def name_generator(application_name):
    if application_name in web_pages:
        return web_pages[application_name].render()
    else:
        abort(404)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return web_pages["login"].render()
    elif request.method=="POST":
        if len(request.form["username"]) is not None\
            and len(request.form["password"]) is not None:
            if verify_password(request.form["username"],
                               request.form["password"]):
                #Set the session "username" key to the username put into the form
                session["username"] = request.form["username"]
                return redirect(url_for("home"))
            else:
                return redirect(url_for("login"))


@app.route("/sign_out")
def sign_out():
    if request.method=="GET":
        session.pop("username", None)
        return redirect("/")