import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

my_map = folium.Map(location=[39, -99], zoom_start=5, tiles="OpenStreetMap")

# lat = list(data.iloc[:, 8])
# lon = list(data.iloc[:, 9])
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
stat = list(data["STATUS"])


def color_picker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'


html = """<h4>Volcano information:</h4>
Name: %s <br>
Status: %s <br>
Height: %s m
"""

fg_p = folium.FeatureGroup(name="Population")

fg_p.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                              style_function=lambda x: {'fillColor': 'green'
                              if x["properties"]["POP2005"] < 1000000
                              else 'blue' if 1000000 <= x["properties"]['POP2005'] < 2000000
                              else 'red', 'fillOpacity': 0.6}))

fg_v = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, na, st in zip(lat, lon, elev, name, stat):
    iframe = folium.IFrame(html=html % (str(na), str(st), str(el)), width=200, height=100)
    # fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe),
    #                            icon=folium.Icon(color=color_picker(el))))
    fg_v.add_child(
        folium.CircleMarker(location=(lt, ln), radius=9, popup=folium.Popup(iframe),
                            fill_color=color_picker(el),
                            color='grey', fill_opacity=0.8))

my_map.add_child(fg_p)
my_map.add_child(fg_v)
my_map.add_child(folium.LayerControl())

my_map.save("Map1_advanced.html")
