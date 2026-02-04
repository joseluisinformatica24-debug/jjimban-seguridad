import time
import redis
from flask import Flask

app = Flask(__name__)
# Conexión a Redis (usamos el nombre del servicio definido en docker-compose)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def get_data():
    # Intenta obtener el dato de la caché de Redis
    valor = cache.get('dato_pesado')

    if valor:
        return f"Respuesta desde Redis (Nivel 2): {valor.decode('utf-8')}"

    # Simulación de proceso lento (2-3 segundos)
    time.sleep(2.5)
    resultado = "Información procesada"

    # Guarda en Redis para la próxima vez
    cache.set('dato_pesado', resultado)
    return f"Procesado y guardado en Redis: {resultado}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
