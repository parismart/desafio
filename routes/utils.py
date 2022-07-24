def connect_database(user, password, host, port, database):
    import psycopg2
    connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                database=database)
    return connection

def close_connect(connection, cursor):
    if (connection):
        cursor.close()
        connection.close()

def json_poi(pois):
    points = []
    for poi in pois:
        point={}
        point['poi_id'] = int(poi[0])
        point['name'] = poi[1]
        point['description_es'] = poi[5]
        point['description_va'] = poi[4]
        point['description_en'] = poi[6]
        point['latitude'] = poi[2]
        point['longitude'] = poi[3]
        point['image'] = poi[7]
        points.append(point)
    return(points)

def get_values(request):
    import datetime
    age = request.GET.get('age', '0')
    gender = request.GET.get('gender', 'None')
    time = request.GET.get('time', '0')
    type = request.GET.get('type', 'None')
    price = request.GET.get('price', 'None')
    difficulty = request.GET.get('difficulty', 'None')
    companions = request.GET.get('companions', 'None')
    transport = request.GET.get('transport', 'None')
    time_stamp = str(datetime.datetime.now().time())
    user_values = (age, gender, time, type, price, difficulty, companions, transport, time_stamp)
    return(user_values)