from flask import Flask, render_template, request
from draw import Draw
import folium
import sys
from flask_restful  import Resource, Api
import sys
import json

app = Flask(__name__)
api = Api(app)

@app.route("/")
def mappy():

	center = [65,11]
	m = folium.Map(location = center, zoom_start = 5)
	Draw().add_to(m)
	m.save("templates/map.html")
	return render_template("index.html")

@app.route('/get_routes', methods = ['POST'])
def get_routes():
    jsdata = request.form['boundaries']

    return json.dumps([{
                      "type": "LineString",
                      "coordinates": [[-100, 40], [-105, 45], [-110, 55]]
                  }, {
                      "type": "LineString",
                      "coordinates": [[-105, 40], [-110, 45], [-115, 55]]
                  }])





if __name__ == "__main__":
	app.run()