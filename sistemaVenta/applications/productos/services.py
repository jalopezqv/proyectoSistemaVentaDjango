import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


def consultar_productos_ms(params={}):
    response = generate_request('http://localhost:5000/productos/consultar-productos', params)

    if response:
        return response

    return ''