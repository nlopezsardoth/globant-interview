import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_weather_endpoint_normal(client):
    response = client.get('/weather?city=Bogota&country=co')
    assert response.status_code == 200
    assert response.json is not None

def test_weather_endpoint_missing_city(client):
    response = client.get('/weather?country=co')
    assert response.status_code == 400
    assert response.json == {'error': 'Missing city or country'}

def test_weather_endpoint_invalid_city(client):
    response = client.get('/weather?city=100&country=co')
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid city name'}

def test_weather_endpoint_invalid_country_alp(client):
    response = client.get('/weather?city=bogota&country=10')
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid country name'}

def test_weather_endpoint_invalid_country_len(client):
    response = client.get('/weather?city=bogota&country=colombia')
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid country name'}
