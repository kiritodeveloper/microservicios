import productos
import os

if __name__ == "__main__":
    host = os.environ.get('API_HOST', '0.0.0.0')
    puerto = os.environ.get('API_PORT',  3001)
    try:
        productos.iniciar_aplicacion().run(host=host, port=puerto, debug=True)
    except Exception as e:
        print("Problemas al conectar con base de datos: "+str(e))
