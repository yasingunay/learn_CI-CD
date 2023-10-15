import pytest
from app import app

@pytest.fixture # aim to create a fixture that will be used by all the tests 
def client():
    app.config['TESTING'] = True # set the TESTING configuration flag to True
    with app.test_client() as client: 
        yield client 

def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!' # b'Hello, World!' is the expected response data