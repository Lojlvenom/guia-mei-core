from http import client
from pydoc import cli
from urllib import response
from fastapi import File
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {
        "message":"Bem vindo a API do projeto Guia Mei Manaus! Para acessar a documentação desta API assim como suas funcionalidades principais acesse o endereço /docs"
    }

def test_pdf_file_response():
    f = open("files/guia.pdf", "r")
    response = client.get('/')
    assert response.content == f.read()