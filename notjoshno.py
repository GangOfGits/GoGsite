from flask import Flask, render_template, request, session, redirect

from login import verifyuserexists, verifypassword, generatehash

app = Flask(__name__,
            static_url_path=""
            )

app.config["SECRET_KEY"] = "totallysecret"

#A fucnction used to generate variables for render_template
def getrendervariables(pagetitle):

    ##The title variable is used for the <title> HTML tag
    title = pagetitle
    #The username variable is taken from the session
    username = session["username"]
    ##The loggedinmessage variable is displayed in the navbar in layout.html
    #It is equal to the session's "username" key, e.g. "admin"
    #If the session has no username key i.e. the user is not logged in, then return "Not currently logged in"
    loggedinmessage = ("Logged in as: " + username) if session["username"] is not None else "Not currently logged in"

    #Returns the variables as a tuple
    return title, loggedinmessage

    #All @app.route decorated 'render' functions should have the following line of code at the start of the function:
    #_title, _loggedinmessage = getrendervariables(%TITLESTRING%)

#RENDER FUNCTION
@app.route("/", methods=["GET"])
def renderhome():
    _title, _loggedinmessage = getrendervariables("Home")

    return render_template("main.html", title=_title, loggedinmessage=_loggedinmessage)

#RENDER FUNCTION
@app.route("/namegenerator", methods=["GET"])
def rendernamegenerator():
    _title, _loggedinmessage = getrendervariables("Name Generator")

    return render_template("namegenerator.html", title=_title, loggedinmessage=_loggedinmessage)

#RENDER FUNCTION
@app.route("/reset", methods=["GET"])
def renderreset():
    _title, _loggedinmessage = getrendervariables("Reset")
    session["username"] = None
    return redirect("/")

#POST FUNCTION
@app.route("/login", methods=["POST"])
def login():
    #If both form inputs have text in them
    if len(request.form["username"]) is not None and len(request.form["password"]) is not None:
        #If the login details are correct
        if verifypassword(request.form["username"], request.form["password"]):
            #Set the session "username" key to the username put into the form
            session["username"] = request.form["username"]
            #Redirect the user to the homepage
            return redirect("/")
        else:
            return redirect("/login")

#RENDER FUNCTION
@app.route("/login", methods=["GET"])
def renderlogin():
    _title, _loggedinmessage = getrendervariables("Login")
    return render_template("login.html", title=_title, loggedinmessage=_loggedinmessage)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
