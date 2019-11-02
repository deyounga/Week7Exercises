#Latitude and Longitude exercise with Shapely and Fiona

import csv
from shapely.geometry import Point, mapping
from fiona import collection

schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }
with collection(
    "countries.shp", "w", "ESRI Shapefile", schema) as output:
    with open('countries.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['longitude']), float(row['latitude']))
            output.write({
                'properties': {
                    'name': row['name']
                },
                'geometry': mapping(point)
            })
