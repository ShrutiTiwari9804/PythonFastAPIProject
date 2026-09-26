from fastapi.testclient import TestClient
from main_test import app


client = TestClient(app)

#Test home api

def test_home ():
    response = client.get("/")
    #Status code check
    assert response.status_code == 200
    # Response data check
    assert response.json () == {"message": "hello shruti"}

# Test ADD API
def test_add():
    response = client.get("/add?a=40&b=50")

    assert response.status_code == 200
    assert response.json() == {"result": 90}