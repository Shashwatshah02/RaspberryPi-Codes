import geocoder
g = geocoder.ip('me')
print(str(g.latlng[0]))
print(str(g.latlng[1]))