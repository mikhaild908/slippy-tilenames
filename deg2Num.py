# slippy map tilenames

import math

def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)

#Phoenix: 33.5467, -112.0456

#results = deg2num(33.5467, -112.0456, 10) # https://a.tile.openstreetmap.org/10/193/410.png
results = deg2num(33.5467, -112.0456, 9) # https://a.tile.openstreetmap.org/9/96/205.png

print (results)