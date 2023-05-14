import json
from threading import local

from plotly.graph_objs import Scattergeo, Layout #1
from plotly import offline

#Explore the structure of the data.
filename = '../data/eq_data_30_days_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#Map the earthquakes.
#data = [Scattergeo(lon=lons, lat=lats)] #2
#Cách khác để xác định dữ liệu cho biểu đồ:
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{ #1
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes') #3
fig = {'data': data, 'layout': my_layout} #4
offline.plot(fig, filename='global_earthquakes.html')

print(mags[:10])
print(lons[:5])
print(lats[:5])