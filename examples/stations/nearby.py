from meteostat import Stations
from datetime import datetime

# Closest weather station for position
stations = Stations(lat = 50, lon = 8, hourly = datetime(1940, 1, 1))
station = stations.fetch(1).to_dict('records')[0]

print('Closest weather station at coordinates 50, 8:')
print(station["name"])
