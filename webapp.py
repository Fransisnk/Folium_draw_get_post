from flask import Flask, render_template, request
import folium
from folium.plugins import Draw
from flask_restful  import Api
import json
from draw_template import _template
app = Flask(__name__)
api = Api(app)


@app.route("/")
def mappy():
    center = [65, 11]
    m = folium.Map(location=center, zoom_start=5)
    Draw._template = _template
    Draw().add_to(m)
    m.save("templates/map.html")
    return render_template("index.html")


@app.route('/get_routes', methods=['POST'])
def get_routes():
    jsdata = request.form['boundaries']
    return json.dumps(jsdata)


if __name__ == "__main__":
    app.run()
