import pytest
import json
from flask.testing import FlaskClient

def test_api_login_user(client: FlaskClient):
    response = client.post('/api/v3/merchant/user/login', json={
        'username': 'email',
        'email': 'password'
    })
    assert response.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(response.get_data(as_text=True))


def test_api_transaction(client: FlaskClient):
    response = client.post('/api/v3/transactions/report', json={
        'fromDate': '2022-12-11',
        'toDate': '2022-12-14',
        'merchant': 1,
        'acquirer': 2
    })
    assert response.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(response.get_data(as_text=True))
    
# -------------------------------------------------------------------------

# import pytest
# import json
# from flask.testing import FlaskClient
# from app import app


# @pytest.fixture
# def client():
#     return app.test_client()

# def test_api_login_user(client: FlaskClient):
#     response = client.post('localhost:5000/api/v3/merchant/user/login', json={
#         'username': 'email',
#         'email': 'password'
#     })
#     assert response.status_code == 200


# def test_api_transaction(client: FlaskClient):
#     response = client.post('localhost:5000/api/v3/transactions/report', json={
#         'fromDate': '2022-12-11',
#         'toDate': '2022-12-14',
#         'merchant': 1,
#         'acquirer': 2
#     })
#     assert response.status_code == 200