# Endpoint Get All Routes:
https://api-routes-data.herokuapp.com/getRoutes/

# Endpoint Get All Point of Interest:
https://api-routes-data.herokuapp.com/getPoi/

# Endpoint Get Route By ID:
https://api-routes-data.herokuapp.com/getRouteById/?id=24

Return: {"error": "ID not found"}

# Endpoint Get Point of Interes By ID:
https://api-routes-data.herokuapp.com/getPoiById/?id=42

Return: {"error": "ID not found"}

# Endpoint Get Recommended Route:
https://api-routes-data.herokuapp.com/getRecommendation/?id=42

Return: {"recommended_route_id": 42}
Return: {"error": "ID not found"}

# Endpoint Post User:
https://api-routes-data.herokuapp.com/postUser/

Admite mayusculas, minusculas y acentos

Return: {"user_id": 42}
Return: {"name_parameter": "Invalid parameter"}

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