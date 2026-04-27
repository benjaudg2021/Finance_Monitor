'''
Goal del development es tener una interfaz grafica que obetenga el valor de la accion listada y poder visualizarla en tiempo real con un refresque elegido:
cada 5 segundos, 15, 30, 60, 5 min, 10, 15, etc.
Ademas de la lsita de acciones, y seteo del refresque de info, la app sera capaz de notificar ciertos casos, como cuando la accion alcance cierto valor
Interfaz grafica dirigida a Samsung Galaxy watch 6 classic
'''


import yfinance as yf
import time
from datetime import datetime

def monitorear_accion(ticket_simbolo):
    # ticket_simbolo podría ser:
    # "MSTR" para NYSE
    # "MSTR.MX" para BMV
    accion = yf.Ticker(ticket_simbolo)
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
            
            # 5. Pausa de 30 segundos
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    # Puedes cambiar 'MSTR' por cualquier otro ticker como 'TSLA' o 'AAPL'
    monitorear_accion("MSTR")

#eliminacion de comentarios creados desde las originales 3 branches de prueba
