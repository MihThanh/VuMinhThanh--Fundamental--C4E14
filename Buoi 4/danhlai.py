from haversine import haversine
city_list = [
    {
        'name' : 'Hà Nội',
        'lat' : 21.0277644,
        'long' : 105.83415979999995,
    },
    {
        'name' : 'Đà Nẵng',
        'lat' : 16.0544068,
        'long' : 108.20216670000002,
    },
    {
    'name' : 'Nha Trang',
    'lat' : 12.2387911,
    'long' : 109.19674880000002,
    },
    {
    'name' : "Thành phố Hồ Chí Minh",
    'lat' : 10.8230989,
    'long' : 106.6296638,
    }
]
for i in range(len(city_list)):
    for j in range(i + 1, len(city_list)):
        cord1 = (city_list[i]['lat'], city_list[i]['long'])
        cord2 = (city_list[j]['lat'], city_list[j]['long'])
        kc = haversine(cord1, cord2)
        print("Khoảng cách từ {0} đến {1} là: {2}".format(city_list[i]['name'],city_list[j]['name'], kc))
