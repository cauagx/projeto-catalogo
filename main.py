from fastapi import fastapi
from fastapi.staticfiles import staticfiles
import os

app = fastapi()

# Simulando um banco de dados 
CATALOGO = [
    {"id": 1, "nome": "Notebook Dell", "preço": 4500.00},
    {"id": 2, "nome": "Mouse Sem Fio", "preço": 120.00},
    {"id": 3, "nome": "Teclado Mecânico", "preço": 350.00},
    {"id": 4, "nome": "Monitor IPS 24", "preço": 850.00}

]

@app.get("/api/itens")
def listar_itens():
    return CATALOGO

# Serve a pasta 'static' onde ficará o frontend (html)
app.mount("/", staticfiles(directory="static", html=true), name="static")    
