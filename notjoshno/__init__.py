from flask import Flask
from notjoshno.authentication import user_exists, verify_password, generate_hash

app = Flask(__name__,
            static_url_path=""
            )

app.config["SECRET_KEY"] = "totallysecret"

from notjoshno import approutes, errorhandlers
