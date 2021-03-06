from meteostat import Stations

# Get number of stations in northern hemisphere
stations = Stations(bounds = [90, -180, 0, 180])

print('Stations in northern hemisphere:')
print(stations.count())

# Get number of stations in southern hemisphere
stations = Stations(bounds = [0, -180, -90, 180])

print('Stations in southern hemisphere:')
print(stations.count())
