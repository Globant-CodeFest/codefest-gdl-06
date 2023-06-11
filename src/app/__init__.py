import os
import json
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
    filename = make_geojson()
    df = geopandas.read_file(filename=filename)

    folium.GeoJson(df, name="geojson").add_to(m)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as map_file:
        m.save(map_file.name)
        return map_file.name


def make_geojson():
    # Create an empty list to store the polygon coordinates
    polygon_features = []
    # Iterate over the stations
    for station in data["stations"]:
        latitude = float(station["latitude"])
        longitude = float(station["longitude"])

        # Check if the polygon feature list is empty or if the current polygon has reached the maximum number of coordinates
        if (
            not polygon_features
            or len(polygon_features[-1]["geometry"]["coordinates"][0]) >= 3
        ):
            # Create a new polygon feature
            polygon_feature = {
                "type": "Feature",
                "properties": {},
                "geometry": {"coordinates": [[]], "type": "Polygon"},
            }
            polygon_features.append(polygon_feature)

        # Add the current coordinate to the last polygon feature
        polygon_features[-1]["geometry"]["coordinates"][0].append([longitude, latitude])

    # Create the GeoJSON feature collection
    geojson_data = {"type": "FeatureCollection", "features": polygon_features}

    # Save the geojson data to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".geojson") as geojson_file:
        geojson_file.write(json.dumps(geojson_data).encode("utf-8"))
        return geojson_file.name
