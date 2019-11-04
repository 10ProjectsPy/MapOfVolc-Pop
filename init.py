import folium
import pandas
map = folium.Map(location = [34.027773, -84.133049], zoom_start= 5, tiles = 'Stamen Terrain')
def color_producer(el):
    if 2000<=el<=3000:
        color = 'yellow'
    elif el>3000:
        color = 'red'
    else:
        color = 'blue'
    return color
fgv = folium.FeatureGroup(name='Volcanoes')
# fg.add_child(folium.Circle(location=[34.027773, -84.133049], popup="Hi there", color='blue', radius=4))
### add volcanoes start
volcanoes = pandas.read_csv('Volcanoes.txt')
elevation = list(volcanoes['ELEV'])
volc_name = list(volcanoes["NAME"])
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])

for lt,ln,el,nm in zip(lat,lon,elevation,volc_name):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],popup=f"Name: {nm} Elevation: {el}",
    color="grey", fill = True,fill_opacity = 0.7, fill_color=color_producer(el), radius = 5))
map.add_child(fgv)
### end adding volcanoes
### add world start
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10**6 
else "blue" if 10**6 < x['properties']['POP2005']<=10**7 
else "yellow" if 10**7< x['properties']['POP2005']<=2*(10**8)
else "red"}))
### add world end
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('NewMap.html')
# folium.Icon()