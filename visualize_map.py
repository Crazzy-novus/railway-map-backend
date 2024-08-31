import folium
import geojson

# Step 1: Load the GeoJSON file
with open('E:/temporary files\sih/backend\india-land-simplified.geojson', 'r') as file:
    geojson_data = geojson.load(file)

# Step 2: Create a folium map centered on the area of interest
# Adjust the coordinates and zoom level as needed
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5, tiles='OpenStreetMap')

# Step 3: Add the GeoJSON overlay to the map
folium.GeoJson(geojson_data, name="GeoJSON Overlay").add_to(m)

# Step 4: Add markers to the map
# Example markers: you can add as many as you like with different coordinates
marker_locations = [
    {"name": "New Delhi", "coordinates": [28.6139, 77.2090]},
    {"name": "Mumbai", "coordinates": [19.0760, 72.8777]},
    {"name": "Bengaluru", "coordinates": [12.9716, 77.5946]},
    {"name": "Chennai", "coordinates": [13.0827, 80.2707]},
]

for location in marker_locations:
    folium.Marker(
        location=location["coordinates"],
        popup=location["name"],
        tooltip=f"Click for more info on {location['name']}"
    ).add_to(m)

# Step 5: Add layer control to toggle overlays and markers
folium.LayerControl().add_to(m)

# Step 6: Save the map to an HTML file or display it in a Jupyter notebook
m.save('map.html')

# If you're in a Jupyter notebook, you can display the map inline using:
# m
