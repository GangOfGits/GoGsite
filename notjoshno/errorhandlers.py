from notjoshno import app
from flask import render_template

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
