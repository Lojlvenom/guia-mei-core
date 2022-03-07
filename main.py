from fastapi import FastAPI
from fastapi.responses import FileResponse 

conf = {
    "title": "Guia Mei Manaus",
    "version":"0.0.1"
}

app = FastAPI(**conf)

@app.get('/guia-pdf', tags=["files"])
def pdf():
    file_path = "files/guia.pdf"
    return FileResponse(file_path)