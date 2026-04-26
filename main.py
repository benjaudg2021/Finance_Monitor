import yfinance as yf
import time
from datetime import datetime

def monitorear_accion(ticket_simbolo):
    print(f"--- Iniciando monitoreo de {ticket_simbolo} ---")
    
    try:
        while True:
            # 1. Obtener los datos de la acción
            accion = yf.Ticker(ticket_simbolo)
            
            # 2. Extraer el precio actual (usamos 'fast_info' para velocidad)
            datos = accion.fast_info
            precio_actual = datos['last_price']
            
            # 3. Obtener la hora actual
            ahora = datetime.now().strftime("%H:%M:%S")
            
            # 4. Mostrar el resultado
            print(f"[{ahora}] Precio de {ticket_simbolo}: ${precio_actual:.2f}")
            
            # 5. Pausa de 1 minuto (60 segundos)
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    # Puedes cambiar 'MSTR' por cualquier otro ticker como 'TSLA' o 'AAPL'
    monitorear_accion("MSTR")

   

   #COMENDARIO HECHO EN LINEA 37 EN BRANCH 3