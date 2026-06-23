from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/producto/1002732")
    assert response.status_code == 200
    assert response.json() == {
        "nombre": "string",
        "codigo_de_barras": "string",
        "precio": "0.00",
        "id": 0,
        "nombre_usuario": "string",
        "nombre_categoria": "string"
    }
