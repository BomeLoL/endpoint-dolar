from fastapi import FastAPI
from datetime import datetime
import urllib.request
import json

app = FastAPI()

def consultar_dolar_api(tipo):
    """Función para traer los datos de ve.dolarapi.com"""
    try:
        url = f"https://ve.dolarapi.com/v1/dolares/{tipo}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get("promedio")
    except Exception as e:
        print(f"Error consultando {tipo}: {e}")
        return None

@app.get("/tasas")
def obtener_tasas():
    # Consultamos ambos endpoints de DolarApi
    precio_bcv = consultar_dolar_api("oficial")
    precio_monitor = consultar_dolar_api("paralelo")

    return {
        "fecha": datetime.now().strftime("%d-%m-%Y"),
        "bcv": precio_bcv,
        "monitor": precio_monitor
    }