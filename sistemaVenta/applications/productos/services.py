from ast import arg
import requests

def generate_request_get(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def generate_request_post(url, json_parametro):
    response = requests.post(url,json=json_parametro)

    if response.status_code == 200:
        return response.json()

def generate_request_put(url,json_parametros={}):
    response = requests.put(url,json=json_parametros)

    if response.status_code == 200:
        return response.json()




def consultar_productos_ms():
    response = generate_request_get('http://localhost:5000/productos/consultar-productos')

    if response:
        return response

    return ''

def crear_producto_ms(json_parametro):
    response = generate_request_post('http://localhost:5000/productos/crear-producto', json_parametro)

    if response:
        return response

    return ''

def inhabilitar_producto_ms(params):
    response = generate_request_put(f'http://localhost:5000/productos/inhabilitar-producto/{params}')

    if response:
        return response

    return ''

def actualizar_producto_ms(json_parametro,id):
    response = generate_request_put(f'http://localhost:5000/productos/actualizar-producto/{id}', json_parametro)

    if response:
        return response

    return ''