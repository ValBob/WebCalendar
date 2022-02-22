from flask import Flask

app = Flask('main')
app.app_context()

city_dict = {10001: "New York",
             20001: "Washington",
             101000: "Moscow"}


@app.route('/index/<int:index>')
def render_city(index):
    if city_dict.get(index):
        return city_dict[index]
    return 'There is no city with this index'
