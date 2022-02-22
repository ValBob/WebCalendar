from flask import Flask, make_response

app = Flask('main')


@app.route('/<string>')
def main_view(string):
    return make_response(string, 204)
