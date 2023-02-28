import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
# lat = list(data.iloc[:, 8])
# lon = list(data.iloc[:, 9])
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[39, -99], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Name")

for lt, ln, ev in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(ev)+" m", icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("Map1.html")
