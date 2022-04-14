from geopy import distance
from math import sin, cos, sqrt, atan2, radians
from sklearn.neighbors import DistanceMetric
import osrm
import numpy as np

lat1, lon1, lat2, lon2, R = 20.9467,72.9520, 21.1702, 72.8311, 6373.0
coordinates_from = [lat1, lon1]
coordinates_to = [lat2, lon2]


#Using haversine
dlon = radians(lon2) - radians(lon1)
dlat = radians(lat2) - radians(lat1)
a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
distance_haversine_formula = R * c
print('distance using haversine formula: ', distance_haversine_formula)

#Using haversine with sklearn
dist = DistanceMetric.get_metric('haversine')

X = [[radians(lat1), radians(lon1)], [radians(lat2), radians(lon2)]]
distance_sklearn = R * dist.pairwise(X)
print('distance using sklearn: ', np.array(distance_sklearn).item(1))



#Using OSRM
osrm_client = osrm.Client(host='http://router.project-osrm.org')
coordinates_osrm = [[lon1, lat1], [lon2, lat2]]  # note that order is lon, lat

osrm_response = osrm_client.route(coordinates=coordinates_osrm, overview=osrm.overview.full)
dist_osrm = osrm_response.get('routes')[0].get('distance') / 1000  # in km
print('distance using OSRM: ', dist_osrm)

#Using geopy
distance_geopy = distance.distance(coordinates_from, coordinates_to).km
print('distance using geopy: ', distance_geopy)

distance_geopy_great_circle = distance.great_circle(coordinates_from, coordinates_to).km
print('distance using geopy great circle: ', distance_geopy_great_circle)















