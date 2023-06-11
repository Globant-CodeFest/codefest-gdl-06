import os
import statistics
import tempfile

from flask import Flask, abort, render_template, send_from_directory, url_for
import folium
import geopandas

from .models.locations import Locations
from .data import data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html", type="Home", proyecto="Industria")

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html", type="Home", proyecto="Industria")


@app.route("/map")
def insights():
    locations = []
    for location in data["stations"]:
        locations.append(
            Locations(
                location["id"],
                location["name"],
                (location["latitude"], location["longitude"]),
            )
        )
    map_file = create_map(locations)
    map_url = url_for("folium_map", filename=os.path.basename(map_file))
    # print(map_url)
    return render_template(
        "index.html",
        type="Mapa",
        map_url=map_url,
    )


@app.route("/tmp/<path:filename>")
def folium_map(filename):
    file_path = os.path.join(tempfile.gettempdir(), filename)
    directory = tempfile.gettempdir()
    if os.path.isfile(file_path) and filename.endswith(".html"):
        return send_from_directory(directory, filename)
        # uncomment the following to delete temp files after rendering.
        # return send_from_directory(directory, filename), os.remove(
        #     os.path.join(directory, filename)
        # )
    else:
        abort(404)


def create_map(locations):
    # Convert the list of Locations to a list of coordinates
    coordinates_str = [location.coordinates for location in locations]

    # Convert the strings to floats
    coordinates = [(float(lat), float(lon)) for lat, lon in coordinates_str]

    # Calculate the mean of the coordinates
    mean_lat = statistics.mean(lat for lat, lon in coordinates)
    mean_lon = statistics.mean(lon for lat, lon in coordinates)

    start_coords = (mean_lat, mean_lon)
    m = folium.Map(location=start_coords, zoom_start=4)
    tooltip = "Click here!"
    for i, location in enumerate(locations):
        folium.Marker(
            coordinates_str[i], popup=location.city_name, tooltip=tooltip
        ).add_to(m)
    # add geojson data
    df = geopandas.read_file(
        url_for("static", filename="geojson/stations.geojson", _external=True)
    )

    folium.GeoJson(df, name="geojson").add_to(m)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as map_file:
        m.save(map_file.name)
        return map_file.name
