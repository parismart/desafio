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
    from unidecode import unidecode
    age = int(request.GET.get('age', '1985'))
    gender = unidecode(request.GET.get('gender', 'otro').lower().strip())
    time = int(request.GET.get('time', '90'))
    route_type = unidecode(request.GET.get('route_type', 'historica').lower().strip())
    price = unidecode(request.GET.get('price', 'gratis').lower().strip())
    difficulty = unidecode(request.GET.get('difficulty', 'baja').lower().strip())
    companions = unidecode(request.GET.get('companions', 'solo').lower().strip())
    transport = unidecode(request.GET.get('transport', 'a pie').lower().strip().replace('-',' '))
    time_stamp = str(datetime.datetime.now())
    user_values = (age, gender, time, route_type, price, difficulty, companions, transport, time_stamp)
    return(user_values)

def check_values(values):
    error = {}
    if values[0] > 2022:
        error['age'] = "Hey Doc. Nos veremos a la 1:15 a.m. en el Centro Comercial Twin Pines."
    if values[0] < 1900:
        error['age'] = "Now he's dead!!!"
    if (values[1] != "hombre") & (values[1] != "mujer") & (values[1] != "otro"):
        error['gender'] = "Invalid parameter"
    if (values[2] < 0) | (values[2] > 480):
        error['time'] = "Invalid parameter"
    if (values[3] != "historica") & (values[3] != "turistica") & (values[3] != "literaria") & (values[3] != "patrimonio"):
        error['route_type'] = "Invalid parameter"
    if (values[4] != "gratis") & (values[4] != "1-50") & (values[4] != "+50"):
        error['price'] = "Invalid parameter"
    if (values[5] != "baja") & (values[5] != "alta"):
        error['difficulty'] = "Invalid parameter"
    if (values[6] != "solo") & (values[6] != "pareja")& (values[6] != "familia") & (values[6] != "amigos"):
        error['companions'] = "Invalid parameter"
    if (values[7] != "a pie") & (values[7] != "bicicleta"):
        error['transport'] = "Invalid parameter"
    return error
    

def mapping(x):
    if x == 'gratis':
        return 1
    elif x == '1-50':
        return 2
    elif x == '+50':
        return 3
    else:
        return 9999

def mapping_age(x):
    if (x > 2004):
        return "0-18"
    elif (x < 2004) & (x > 1987):
        return "18-35"
    elif (x < 1987) & (x > 1977):
        return "35-45"
    else:
        return "+45"