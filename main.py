from flask import Flask, jsonify
import geojson

app = Flask(__name__)

@app.route('/geojson')
def get_geojson():
    # Load the GeoJSON file
    with open("E:/temporary files\sih/backend\india-land-simplified.geojson", 'r') as file:
        geojson_data = geojson.load(file)
    return jsonify(geojson_data)

@app.route('/markers')
def get_markers():
    # Example marker data
    markers = [
        {"name": "New Delhi", "coordinates": [28.6139, 77.2090]},
        {"name": "Mumbai", "coordinates": [19.0760, 72.8777]},
        {"name": "Bengaluru", "coordinates": [12.9716, 77.5946]},
        {"name": "Chennai", "coordinates": [13.0827, 80.2707]},
    ]
    return jsonify(markers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
