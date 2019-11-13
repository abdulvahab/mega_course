import folium
import pandas as pd
import matplotlib.pyplot as plt

map=folium.Map(location=[43.978802, -121.681], tiles="Stamen terrain")
fgv = folium.FeatureGroup(name="Volcanoes Points")
fgp = folium.FeatureGroup(name="World Population")

df = pd.read_csv("Volcanoes.txt")
#center = df["NAME"]=="Bachelor"
#print(df[center])
lat=list(df["LAT"])
lon=list(df["LON"])
name=list(df["NAME"])
elev=list(df["ELEV"])
vol_type = list(df["TYPE"])

def color_generator(elevation):
    if elevation <= 1000:
        color="green"
    elif 3000 >= elevation >1000:
        color="orange"
    else:
        color="red"
    return color

#df["ELEV"].plot(kind="hist", bins=8 )
#plt.xlabel("Elevation") 
#plt.show()
#print(lat)
#print(lon)
#print(NAME)

#df1=pd.read_csv("world.json")
#print(df1.head())

geom = zip(lat,lon, name, elev, vol_type)
#print(type(geom))
for lt,lo,na,el,ty in geom:
    html = f'''Volcano name:<br>
<a href="https://www.google.com/search?q=%22{na}%20volcano%22" target="_blank">{na}</a><br>
Height: {el} m<br>Type:{ty}'''
    iframe = folium.IFrame(html=html, width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, lo],radius=10, popup=folium.Popup(iframe),  fill_color=color_generator(el),color="grey", fill_opacity=0.7))

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] > 100000000 else 'red' }))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map9.html")
