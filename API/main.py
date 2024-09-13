import json
import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Models.Clima import Clima


API_KEY ="9e82ed814559493da07191112240309"
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
clima = Clima(API_KEY, 53, -0.12)

"""
<------------------>
<-------RUTAS------>
<------------------>
"""
@app.get("/")
def root():
    return "Conexion correcta"

@app.get("/clima")
async def obtener_clima_ubicacion():
    return clima.obtener_clima()