import urllib.request as url
import urllib.error as error
import json

class Clima:
    def __init__(self, API_KEY, latitud, longitud):
        """
        :param API_KEY:
        :type API_KEY: Llave que da la api del clima, recordar tiene 5millones de llamadas
        :param latitud:
        :type latitud: Latitud del dispositivo
        :param longitud:
        :type longitud: Latitud del dispositivo
        """
        self.API_KEY = API_KEY
        self.latitud = latitud
        self.longitud = longitud
        self.url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}"
    def modificar_coordenadas(self, latitud:float, longitud:float):
        self.latitud = latitud
        self.longitud = longitud
    def obtener_clima(self)->dict:
        try:
            with url.urlopen(self.url+f"&q={self.latitud},{self.longitud}&aqi=no") as response:
                data = response.read().decode('utf-8')
                json_data:dict = json.loads(data)
                return json_data
        except error.HTTPError as e:
            print(f"ERROR HTTP: {e.code} ~ {e.reason}")
        except error.URLError as e:
            print(f"ERROR URL: {e.reason}")
        except json.JSONDecodeError:
            print(f"ERROR JSON")
        except Exception:
            print("ERROR: Desconocido")
