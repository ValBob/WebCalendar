from flask import Flask, render_template

app = Flask('main')
app.app_context()


@app.route('/help')
def render_help():
    return render_template("help.html")


@app.route('/info')
def render_info():
    return render_template("info.html")
