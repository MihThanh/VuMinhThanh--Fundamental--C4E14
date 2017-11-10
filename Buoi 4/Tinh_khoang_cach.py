from haversine import haversine

# ha_noi = {
#     'Name' : 'Hà Nội',
#     'Lat' : 21.0277644,
#     'Long' : 105.83415979999995,
# }
#
# da_nang = {
#     'Name' : 'Đà Nẵng',
#     'Lat' : 16.0544068,
#     'Long' : 108.20216670000002,
# }
# tphcm = {
#     'Name' : 'Thành phố Hồ Chí Minh',
#     'Lat' : 10.8230989,
#     'Long' : 106.6296638,
# }
# paris = {
#     'Name' : 'Paris',
#     'Lat' : 48.856614,
#     'Long' : 2.3522219000000177,
# }

city_list = [
    {
        'Name' : 'Hà Nội',
        'Lat' : 21.0277644,
        'Long' : 105.83415979999995,
    },
    {
        'Name' : 'Đà Nẵng',
        'Lat' : 16.0544068,
        'Long' : 108.20216670000002,
    },
    {
        'Name' : 'Thành phố Hồ Chí Minh',
        'Lat' : 10.8230989,
        'Long' : 106.6296638,
    },
    {
        'Name' : 'Paris',
        'Lat' : 48.856614,
        'Long' : 2.3522219000000177,
    }
]
n = len(city_list)
for i in range(n - 1):
    for j in range(i + 1, n):
        city1 = city_list[i]
        city2 = city_list[j]
        cord1 = [city1['Lat'], city1['Long']]
        cord2 = [city2['Lat'], city2['Long']]
        distance = haversine(cord1, cord2)
        print("Khoảng cách từ {0} đến {1} là: {2}: ".format(city1['Name'],city2['Name'],distance))
