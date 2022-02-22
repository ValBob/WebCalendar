from flask import Flask

app = Flask(__name__)


def not_passed_handler(e):
    return "You shall not pass"


app.register_error_handler(403, not_passed_handler)
