import json
from app import app


def test_index_route():
    response = app.test_client().get('/getUser/icidomar15@gmail.com')
    res = json.loads(response.data.decode('utf-8')).get("Usuario")
    Usuario={"Usuario":["Omar Arturo","icidomar15@gmail.com",1]}
    assert response.status_code == 200
    assert res== Usuario["Usuario"]
def test_index_route():
    response = app.test_client().get('/getUser/icidomar15@gmail.com')
    res = json.loads(response.data.decode('utf-8')).get("Usuario")
    Usuario={"Usuario":["Omar Arturo","icidomar15@gmail.com",1]}
    assert response.status_code == 200
    assert res== Usuario["Usuario"]