from fastapi import FastAPI

conf = {
    "title": "Guia Mei Manaus",
    "version":"0.0.1"
}

app = FastAPI(**conf)

@app.get('/')
def home():
    return {
        "message":"deu certo"
    }