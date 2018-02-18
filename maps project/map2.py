import pandas
import folium

df = pandas.read_csv("Volcanoes-USA.txt")
location = df['LAT'].mean(), df['LON'].mean()


map = folium.Map(location=location, zoom_start=4, tiles="Mapbox bright")

locationlist = df[["LAT","LON"]].values.tolist()
labels = df["NAME"].values.tolist()
elevation=df["ELEV"].values.tolist()
elev_mean=df["ELEV"].mean()

df["name and elev"]=df["NAME"]+", "+df["ELEV"].apply(str)
labels2 = df["name and elev"].values.tolist()

def color(elev):
    mean=int(df["ELEV"].mean())
    maxim=int(max(df["ELEV"]))
    minim=int(min(df["ELEV"]))
    step=int((maxim-minim)/3)
    if elev in range (minim,minim+step):
        col='green'
    elif elev in range (minim+step, minim+step*2):
        col='yellow'
    elif elev in range (minim+step*2, minim+step*3):
        col='orange'
    else:
        col='red'
    return col

fg=folium.FeatureGroup(name="Volcano Locations")

for point in range(len(locationlist)):
    popup = folium.Popup(labels2[point], parse_html=True)
    fg.add_child(folium.Marker(locationlist[point], popup=popup, icon=folium.Icon(color=color(elevation[point]))))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open(file="world_population.json").read(),
                             name=("world population"),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save(outfile="map_project.html")
