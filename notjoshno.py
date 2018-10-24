from flask import Flask, render_template, request, session, redirect

from login import verify_user_exists, verify_password, generate_hash

app = Flask(__name__,
            static_url_path=""
            )

app.config["SECRET_KEY"] = "totallysecret"

#A fucnction used to generate variables for render_template
def get_render_variables(pagetitle):

    ##The title variable is used for the <title> HTML tag
    title = pagetitle
    #The username variable is taken from the session, if available
    try:
        username = session["username"]
    except:
        username = None
    ##The logged_in_message variable is displayed in the navbar in layout.html
    #It is equal to the session's "username" key, e.g. "admin"
    #If the session has no username key i.e. the user is not logged in, then return "Not currently logged in"
    logged_in_message = ("Logged in as: " + username) if username is not None else "Not currently logged in"

    #Returns the variables as a tuple
    return title, logged_in_message

    #All @app.route decorated 'render' functions should have the following line of code at the start of the function:
    #_title, _logged_in_message = get_render_variables(%TITLESTRING%)

#RENDER FUNCTION
@app.route("/", methods=["GET"])
def render_home():
    _title, _logged_in_message = get_render_variables("Home")

    return render_template("main.html", title=_title, logged_in_message=_logged_in_message)

#RENDER FUNCTION
@app.route("/namegenerator", methods=["GET"])
def render_name_generator():
    _title, _logged_in_message = get_render_variables("Name Generator")

    return render_template("namegenerator.html", title=_title, logged_in_message=_logged_in_message)

#RENDER FUNCTION
@app.route("/signout", methods=["GET"])
def render_reset():
    _title, _logged_in_message = get_render_variables("Sign Out")
    session["username"] = None
    return redirect("/")

#RENDER FUNCTION
@app.route("/login", methods=["GET"])
def render_login():
    _title, _logged_in_message = get_render_variables("Login")
    return render_template("login.html", title=_title, logged_in_message=_logged_in_message)

#POST FUNCTION
@app.route("/login", methods=["POST"])
def login():
    #If both form inputs have text in them
    if len(request.form["username"]) is not None and len(request.form["password"]) is not None:
        #If the login details are correct
        if verify_password(request.form["username"], request.form["password"]):
            #Set the session "username" key to the username put into the form
            session["username"] = request.form["username"]
            #Redirect the user to the homepage
            return redirect("/")
        else:
            return redirect("/login")


#ERROR HANDLING
@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html", error="403 - Forbidden")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error="404 - Page not found")

@app.errorhandler(410)
def page_deleted(e):
    return render_template("410.html", error="410 - Page deleted")

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", error="500 - Internal Server Error")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
