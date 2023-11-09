ENDPOINT = 'http://127.0.0.1:8000/docs#/default/ '
import requests

def test_can_get():
    response = requests.get(ENDPOINT+'items__get')
    assert response.status_code == 200

def test_post_3_times():
    payload = {"name":"string"}
    for _ in range(3):
        response = requests.put(ENDPOINT+'add__post',json=payload)
        assert response.status_code == 200
