from flask import Flask, request

app = Flask('main')


@app.route('/', methods=['POST', 'GET', 'PUT', 'CREATE'])
def main_view():
    if request.method == 'POST':
        return 'Successfully authorized!'
    elif request.method == 'PUT':
        return 'Successfully published!'
    elif request.method == 'CREATE':
        return 'Created a new web page!'
    return 'Welcome there!'
