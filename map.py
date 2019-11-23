import folium
import pandas
import geometrydata as geodata

if __name__ == '__main__':

    geodata.geodata()

    data=pandas.read_csv("Volcanoes.txt")
    lat=list(data.LAT)
    lon = list(data.LON)
    elev = list(data.ELEV)
    name=list(data.NAME)

    def coloradder(dta):
        if dta<1000:
            return "green"
        elif 1000<=dta<4000:
            return "orange"
        elif str(dta)=="nan":
            return "black" 
        else:
            return "red"
    map=folium.Map(location=[23.2156,72.6369],zoom_start=5,tiles="Mapbox Bright")

    fg=folium.FeatureGroup(name="Volcanoes")
    for i,j,k,x in zip(lat,lon,name,elev):
        fg.add_child(folium.CircleMarker(location=[i,j],radius=6,popup=k,fill_color=coloradder(x),color="grey",fill_opacity=0.7))
    fp=folium.FeatureGroup(name="Population")
    fp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' if int(x['properties']['POP2018']) < 10000000
    else 'orange' if 10000000 <= int(x['properties']['POP2018']) < 20000000 else 'red'}))
    map.add_child(fg)
    map.add_child(fp)
    map.add_child(folium.LayerControl())
    map.save("map.html")