from flask import Flask, request, make_response

app = Flask('main')
URL = '/'


@app.route(URL, methods=['GET', 'POST', 'PUT'])
def main_view():
    if request.method == 'GET':
        return make_response('It\'s all right. This is the main page.', 200)
    return make_response('Not ready yet', 501)
