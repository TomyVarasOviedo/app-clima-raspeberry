import json
import uuid
from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import uvicorn

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
templates = Jinja2Templates(directory="../Client/templates")
clima = Clima(API_KEY, 53, -0.12)

"""
<------------------>
<-------RUTAS------>
<------------------>
"""
@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse(name="index.html",request=request)

@app.get("/clima")
async def obtener_clima_ubicacion():
    return clima.obtener_clima()

@app.post("/display")
async def set_display_clima(humedad:Annotated[str, Form()],temperatura:Annotated[str, Form()], dia:Annotated[str, Form()]):
    return {
        "humedad":humedad,
        "temperatura":temperatura,
        "dia":dia
    }
