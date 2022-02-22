from flask import Flask, make_response
import datetime

app = Flask('main')

@app.route('code_here')
def main_view():
    time = datetime.datetime.now()
    year, month, day = time.year, time.month, time.day

    # your code here