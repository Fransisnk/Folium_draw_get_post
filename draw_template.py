from jinja2 import Template


_template = Template(u"""
            {% macro script(this, kwargs) %}
            // FeatureGroup is to store editable layers.
            var drawnItems = new L.featureGroup().addTo({{this._parent.get_name()}});


            var {{this.get_name()}} = new L.Control.Draw({
                "edit": {"featureGroup": drawnItems}
                });
            {{this._parent.get_name()}}.addControl({{this.get_name()}});
            {{this._parent.get_name()}}.on(L.Draw.Event.CREATED, function (event) {
              var layer = event.layer,
                  type = event.layerType,
                  coords;
              var coords = JSON.stringify(layer.toGeoJSON());
              layer.on('click', function() {
                alert(coords);
                var fs = require("fs");
                fs.writeFile("./coords.json", coords, (err) => {
                    if (err) {
                        console.error(err);
                        return;
                    };
                    alert("File has been created");
                });
                console.log("coords");
                });
               drawnItems.addLayer(layer);
             });
             {{this._parent.get_name()}}.on(L.Draw.Event.DRAWSTOP, function (event) {
             if (drawnItems.getLayers().length == 2)
                  {
                  var points = {start: drawnItems.getLayers()[0].toGeoJSON(),
                                end: drawnItems.getLayers()[1].toGeoJSON()}

                  $.post( "/get_routes", 
                          {
                          boundaries: JSON.stringify(points) 
                          }).done(function( data ) 
                            {
                            L.geoJSON(JSON.parse(data)).addTo({{this._parent.get_name()}});
                            }
                        );          


                  }
             });
            {% endmacro %}
            """)