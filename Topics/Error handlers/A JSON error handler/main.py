from flask import Flask, jsonify
app = Flask(__name__)


def handler_404(e):
    return jsonify({'message': 'Something was not found', 'code': 404})


app.register_error_handler(404, handler_404)
