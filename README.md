# Endpoint Get All Routes:
https://api-routes-data.herokuapp.com/getRoutes/

# Endpoint Get All Point of Interest:
https://api-routes-data.herokuapp.com/getPoi/

# Endpoint Get Route By ID:
https://api-routes-data.herokuapp.com/getRouteById/?id=24

Return :{
  "route_id": "String o Int. ID DE LA RUTA",
  "name": "String. NOMBRE DE LA RUTA",
  "difficulty": "String. DIFICULTAD",
  "image": "String. URL DE LA IMAGEN DE LA RUTA",
  "duration": "Int. DURACIÓN EN MINUTOS",
  "startingPoint": "String PUNTO DE INICIO",
  "endingPoint": "String PUNTO DE FINALIZACIÓN",
  "description_es": "String. DESCRIPCIÓN",
  "description_va": "String. DESCRIPCIÓN",
  "description_en": "String. DESCRIPCIÓN",
  "description": "String. DESCRIPCIÓN",
  "transport": ["String. ETIQUETA"],
  "type": ["String. ETIQUETA"],
  "url": "String. URL DE LA RUTA",
  "pois": [
    {
      "poi_id": "String o Int. ID DEL PUNTO DE INTERÉS",
      "name": "String. NOMBRE DEL PUNTO DE INTERÉS",
      "description_es": "String. DESCRIPCIÓN DEL PUNTO DE INTERÉS",
      "description_va": "String. DESCRIPCIÓN DEL PUNTO DE INTERÉS",
      "description_en": "String. DESCRIPCIÓN DEL PUNTO DE INTERÉS",
      "latitude": "Double. LATITUD DEL PUNTO DE INTERÉS",
      "longitude": "Double. LONGITUD DEL PUNTO DE INTERÉS"
      "image": "String. URL DE LA IMAGEN DEL PUNTO DE INTERÉS",

    }
  ]
}

Si la ID no esta en el rango (1-24)
Return: {"error": "ID not found"}

# Endpoint Get Point of Interes By ID:
https://api-routes-data.herokuapp.com/getPoiById/?id=42

Return: {
      "poi_id": "String o Int. ID DEL PUNTO DE INTERÉS",
      "name": "String. NOMBRE DEL PUNTO DE INTERÉS",
      "description_es": "String. DESCRIPCIÓN DEL PUNTO DE INTERÉS",
      "description_va": "String. DESCRIPCIÓN DEL PUNTO DE INTERÉS",
      "description_en": "String. DESCRIPCIÓN DEL PUNTO DE INTERÉS",
      "latitude": "Double. LATITUD DEL PUNTO DE INTERÉS",
      "longitude": "Double. LONGITUD DEL PUNTO DE INTERÉS"
      "image": "String. URL DE LA IMAGEN DEL PUNTO DE INTERÉS",
    }

Si la ID no esta en el rango (1-293)
Return: {"error": "ID not found"}

# Endpoint Get Recommended Route:
https://api-routes-data.herokuapp.com/getRecommendation/?id=42

Return: {"recommended_route_id": 42}
Return: {"error": "ID not found"}

# Endpoint Post User:
https://api-routes-data.herokuapp.com/postUser/

Admite mayusculas, minusculas y acentos

Return: {"user_id": 42}

Default parameters:
    age = 1985
    gender = 'otro'
    time = 90
    route_type = 'historica'
    price = 'gratis'
    difficulty = 'baja'
    companions = 'pareja'
    transport = 'a pie'

{
    "age": "Int. (1900-2022)",
    "gender": "String. (hombre, mujer, otro) ",
    "time": "Int. (0-480)",
    "route_type": "String. ('historica','literaria','Patrimonio','turistica')", 
    "price": "String. (gratis, 1-50, +50) ",
    "difficulty": "String. (alta, baja)",
    "companions": "String.  (solo, pareja, familia, amigos)",
    "transport": "String.  (a pie, bicicleta)"
}