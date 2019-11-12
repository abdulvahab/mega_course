import folium
import pandas as pd
map=folium.Map(location=[51.72451906194691, -1.2266895307558257], tiles="Stamen terrain")
fg = folium.FeatureGroup(name="My Map")

df = pd.read_csv("Volcanoes.txt")
lat=list(df["LAT"])
lon=list(df["LON"])
#print(lat)
#print(lon)
geom = zip(lat,lon)
#print(type(geom))
coordinates=[]
count = 1
for i,j in geom:
    coordinates.append([i,j])
    fg.add_child(folium.Marker(location=[i, j], popup=f"HI, I am a Marker {count}", icon=folium.Icon(color="blue")))
    count += 1

map.add_child(fg)
map.save("Map4.html")
