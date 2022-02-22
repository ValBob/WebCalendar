from flask import Flask

app = Flask(__name__)

@app.route("/capital/<country>")
def capital(country):

    capitals_dictionary = {
        "Russia":"Moscow",
        "Ukraine":"Kiev",
        "USA":"Washington"
    }

    if not capitals_dictionary.get(country):
        return abort(404, 'Resource not found')
    else:
        return capitals_dictionary.get(country)
