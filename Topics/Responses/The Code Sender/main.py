from flask import Flask, jsonify

app = Flask('main')
app.app_context()


@app.route('/<data>')
def response_maker(data):
    text, code = data.split(';')
    return jsonify({'code': code, 'message': text})

