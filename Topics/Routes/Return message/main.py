from flask import Flask

app = Flask('main')
app.app_context()

@app.route('/about')
def render_about():
    return 'Information about this page'
