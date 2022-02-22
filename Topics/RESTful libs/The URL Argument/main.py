from flask import Flask
from flask import request

app = Flask('main')


@app.route('/storage/images/<filename>', methods=['GET', 'POST'])
def main_view(filename):
    if request.method == 'GET':
        return filename

