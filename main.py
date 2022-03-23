from fastapi import FastAPI
from fastapi.responses import FileResponse 

conf = {
    "title": "Guia Mei Manaus",
    "version":"0.0.1"
}

app = FastAPI(**conf)


@app.get('/', include_in_schema= False)
def home():
    return {
        "message":"Bem vindo a API do projeto Guia Mei Manaus! Para acessar a documentação desta API\
        assim como suas funcionalidades principais acesse o endereço /docs"
    }

@app.get('/guia-pdf', tags=["files"])
def pdf():
    file_path = "files/guia.pdf"
    return FileResponse(file_path)