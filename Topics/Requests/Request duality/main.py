from flask import Flask, request

app = Flask('main')

@app.route('/', methods=['GET', 'POST'])
def main_view():
    if request.method == 'GET':
        return 'I\'m GETting some diamonds...'
    return 'Hey, there is an imPOSTor!'
