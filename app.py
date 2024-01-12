# RESTAPI IS CREATED USING FLASK FRAMEWORK (LIBRARY) BELOW  in app.py file

from flask import Flask, request, jsonify

app=Flask(__name__)


countries=[
    {"id":1,"name":"India","Capital":"Newdelhi","area":508002},
    {"id":2,"name":"Austraila","Capital":"canberra","area":7654321},
    {"id":3,"name":"Thailand","Capital":"Bangkok","area":513120}
]

def _find_next_id():
    return max(country["id"] for country in countries)+1

@app.get("/countries")
def _get_country():
    return jsonify(countries)

@app.post("/countries")
def _add_country():
    if request.is_json:
        country=request.get_json()
        country["id"]= _find_next_id()
        countries.append(country)
        return country,201
    return {"error":"request must be JSON"},415

@app.put("/countries/<int:id>") # here need to pass which item id has to be updated
def _update_country(id):
    #  object = next((x for x in countries  if x['id'] == id), None)
    for x in countries:
        if x['id'] == id:
            object = x
            break
        else:
            object = None
    print(object)
    if object != None:
        object['name'] = request.json['name']
        object['Capital'] = request.json['Capital']
        object['area'] = request.json['area']
        return jsonify(object),200
    else:
        return {"error":"object not found"},404

@app.delete("/countries/<int:id>")
def _delete_country(id):
    for index,x in enumerate(countries):
        if x['id']==id:
            index_to_remove=index
            break
        else:
            index_to_remove=None
    if index_to_remove!=None:
        countries.pop(index_to_remove)
        return {"success":"id deleted "},200

@app.get("/countries/<int:id>") #get by id 
def _get_country_by_id(id):
    for x in countries:
        if x['id']==id:
            object=x
            break
        else:
            object=None
    if object!=None:
        return object
    else:
        return {"error: country not found"},404











