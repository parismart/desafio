from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from routes.utils import *
from routes.db_settings import *
import json

def index(request):
    return render(request, "index.html")

def predict(request):
    import pickle
    import numpy as np
    import pandas as pd

    connection = connect_database(user, password, host, port, database)
    cursor = connection.cursor()
    id = int(request.GET.get('id', '1'))
    # check id
    cursor.execute("SELECT id FROM routes_users;")
    index = cursor.fetchall()
    res = {}
    if (id,) in index:
        cursor.execute(f"""SELECT * FROM routes_users WHERE id = {id}""")
        user_id = cursor.fetchall()
        # Import Model
        filename = 'routes/model/mlp_model.pkl'
        with open(filename, 'rb') as archivo_entrada:
            model = pickle.load(archivo_entrada)
        # Format Array
        user_id = np.array(user_id[0][1:-1]).reshape(1,8)
        # Transform Age
        user_id[0][0]  = mapping_age(int(user_id[0][0]))
        # Transform Time
        user_id[0][2] = int(user_id[0][2])/60
        # To DataFrame
        get_user = pd.DataFrame(data = user_id, index = ['1'], 
        columns = ['age', 'gender', 'time', 'type_route', 'price', 'difficulty', 'accompaniment', 'transport'])    
        # Get Dummies
        get_user = pd.get_dummies(get_user, prefix=['age', 'gender', 'type', 'diff', 'comp', 'trans'], 
        columns=['age', 'gender', 'type_route', 'difficulty','accompaniment', 'transport'])
        features = ['time', 'price', 'age_+45', 'age_0-18', 'age_18-35',
                    'age_35-45', 'gender_hombre', 'gender_mujer',
                    'gender_otro', 'type_historica', 'type_literaria',
                    'type_patrimonio', 'type_turistica', 'diff_alta', 'diff_baja',
                    'comp_amigos', 'comp_familia', 'comp_pareja', 'comp_solo', 'trans_a pie',
                    'trans_bicicleta']
        get_user = pd.DataFrame(data = get_user, columns=features)
        get_user = get_user.fillna(0)
        # Transform Price
        get_user['price'] = get_user['price'].apply(mapping)
        # Prediction
        pred = model.predict(get_user)
        res['recommended_route_id'] = int(pred[0])+1
    else:
        res['error'] = 'ID not found'
    close_connect(connection, cursor)
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def post_user(request):
    connection = connect_database(user, password, host, port, database)
    cursor = connection.cursor()
    values = get_values(request)
    values = check_values(values)
    query = f"""INSERT INTO routes_users(age,
                gender,
                time,
                route_type,
                price,
                difficulty,
                companions,
                transport,
                time_stamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"""
    # if error != {}:
    #     res = error
    # else:
    cursor.execute(query, values)
    connection.commit()
    user_id = cursor.fetchall()
    res = {'user_id':user_id[0][0]}
    close_connect(connection, cursor)

    return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")

def routes(request):
    connection = connect_database(user, password, host, port, database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM routes_rutas ORDER BY id;")
    routes = cursor.fetchall()
    rutas = []
    for idx, route in enumerate(routes):
        ruta={}
        ruta['route_id'] = int(route[0])
        ruta['name'] = route[1]
        ruta['difficulty'] = route[6]
        ruta['image'] = route[9]
        ruta['duration'] = route[5]
        ruta['startingPoint'] = route[7]
        ruta['endingPoint'] = route[8]
        ruta['description_es'] = route[13]
        ruta['description_va'] = route[14]
        ruta['description_en'] = route[15]
        ruta['transport'] = route[11]
        ruta['type'] = route[12]
        ruta['url'] = route[10]
        cursor = connection.cursor()
        query = f'''SELECT * 
        FROM routes_poi as p
        WHERE p.route_id = {idx+1};'''
        cursor.execute(query)
        pois = cursor.fetchall()
        ruta['poi'] = json_poi(pois)
        rutas.append(ruta)
    close_connect(connection, cursor)
    return HttpResponse(json.dumps(rutas, ensure_ascii=False), content_type="application/json")

def route_id(request):
    connection = connect_database(user, password, host, port, database)
    cursor = connection.cursor()
    id = int(request.GET.get('id', '1'))
    query_rutas = f"SELECT id FROM routes_rutas;"
    query_ruta = f"SELECT * FROM routes_rutas WHERE id = {id};"
    query_poi = "SELECT * FROM routes_poi;"
    cursor.execute(query_rutas)
    index = cursor.fetchall()
    ruta={}
    if (id,) in index:
        cursor.execute(query_ruta)
        route = cursor.fetchall()
        cursor.execute(query_poi)
        pois = cursor.fetchall()
        ruta['route_id'] = int(route[0][0])
        ruta['name'] = route[0][1]
        ruta['difficulty'] = route[0][6]
        ruta['image'] = route[0][9]
        ruta['duration'] = route[0][5]
        ruta['startingPoint'] = route[0][7]
        ruta['endingPoint'] = route[0][8]
        ruta['description_es'] = route[0][13]
        ruta['description_va'] = route[0][14]
        ruta['description_en'] = route[0][15]
        ruta['transport'] = route[0][11]
        ruta['type'] = route[0][12]
        ruta['url'] = route[0][10]
        cursor = connection.cursor()
        query = f'''SELECT * FROM routes_poi WHERE route_id = {id};'''
        cursor.execute(query)
        pois = cursor.fetchall()
        ruta['poi'] = json_poi(pois)  
    else:
        ruta['error'] = 'ID not found'
    close_connect(connection, cursor)
    return HttpResponse(json.dumps(ruta, ensure_ascii=False), content_type="application/json")

def poi(request):
    connection = connect_database(user, password, host, port, database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM routes_poi ORDER BY id;")
    pois = cursor.fetchall()
    points = json_poi(pois)
    if (connection):
        cursor.close()
        connection.close()
    return HttpResponse(json.dumps(points, ensure_ascii=False), content_type="application/json")

def poi_id(request):
    connection = connect_database(user, password, host, port, database)
    cursor = connection.cursor()
    id = int(request.GET.get('id', '1'))
    cursor.execute(f'''SELECT * FROM routes_poi WHERE id = {id};''')
    poi = cursor.fetchall()
    cursor.execute("SELECT id FROM routes_poi;")
    index = cursor.fetchall()
    point={}
    if (id,) in index:
        point['poi_id'] = int(poi[0][0])
        point['name'] = poi[0][1]
        point['description_es'] = poi[0][5]
        point['description_va'] = poi[0][4]
        point['description_en'] = poi[0][6]
        point['latitude'] = poi[0][2]
        point['longitude'] = poi[0][3]
        point['image'] = poi[0][7]
    else:
        point['error'] = 'ID not found'
    close_connect(connection, cursor)
    return HttpResponse(json.dumps(point, ensure_ascii=False), content_type="application/json")