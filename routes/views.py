from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import HttpResponse
from routes.utils import *
from routes.db_settings import *
import json

def index(request):
    return render(request, "index.html")

def predict(request):
    import pickle
    connection = connect_database(user, password, host, port, database)
    cursor = connection.cursor()
    id = get_values(request)
    cursor.execute(f"""SELECT * FROM routes_users WHERE id = {id}""")
    user = cursor.fetchall()
    filename = 'finished_model.pkl'
    with open(filename, 'wb') as archivo_entrada:
        model = pickle.load(archivo_entrada)

    predict = model.predict_proba(user)


    close_connect(connection, cursor)
    return HttpResponse(json.dumps({'user_id':user_id[0]}, ensure_ascii=False), content_type="application/json")


# @csrf_token
def post_user(request):
    connection = connect_database(user, password, host, port, database)
    cursor = connection.cursor()
    values = get_values(request)
    query = f"""INSERT INTO routes_users(age,
                gender,
                time,
                type,
                price,
                difficulty,
                companions,
                transport,
                time_stamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id"""
    cursor.execute(query, values)
    connection.commit()
    user_id = cursor.fetchall()
    close_connect(connection, cursor)
    return HttpResponse(json.dumps({'user_id':user_id[0][0]}, ensure_ascii=False), content_type="application/json")

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