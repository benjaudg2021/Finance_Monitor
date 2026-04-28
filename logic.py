'''
Goal del development es tener una interfaz grafica que obetenga el valor de la accion listada y poder visualizarla en tiempo real con un refresque elegido:
cada 5 segundos, 15, 30, 60, 5 min, 10, 15, etc.
Ademas de la lsita de acciones, y seteo del refresque de info, la app sera capaz de notificar ciertos casos, como cuando la accion alcance cierto valor
Interfaz grafica dirigida a Samsung Galaxy watch 6 classic
'''


import yfinance as yf
import time
from datetime import datetime

def monitorear_acciones(simbolos):
    """
    Monitorea múltiples acciones e índices simultáneamente.
    
    Args:
        simbolos (list): Lista de símbolos a monitorear
    """
    print(f"--- Iniciando monitoreo de {len(simbolos)} activos ---")
    print(f"Activos: {', '.join(simbolos)}")
    print("Actualizando cada 30 segundos...\n")
    
    try:
        while True:
            ahora = datetime.now().strftime("%H:%M:%S")
            print(f"\n{'='*70}")
            print(f"[{ahora}] ACTUALIZACIÓN DE PRECIOS")
            print(f"{'='*70}")
            
            # Obtener datos de todos los símbolos
            for simbolo in simbolos:
                try:
                    accion = yf.Ticker(simbolo)
                    datos = accion.fast_info
                    precio_actual = datos.get('last_price', 'N/A')
                    
                    # Obtener información adicional
                    cambio = datos.get('dayChange', 'N/A')
                    cambio_porcentaje = datos.get('dayChangePercent', 'N/A')
                    
                    # Formatear la salida
                    if isinstance(precio_actual, (int, float)):
                        print(f"  {simbolo:15} → ${precio_actual:10.2f}", end="")
                        if isinstance(cambio, (int, float)) and isinstance(cambio_porcentaje, (int, float)):
                            signo = "+" if cambio >= 0 else ""
                            print(f"  ({signo}{cambio:7.2f} | {signo}{cambio_porcentaje:6.2f}%)")
                        else:
                            print()
                    else:
                        print(f"  {simbolo:15} → Error obteniendo datos")
                        
                except Exception as e:
                    print(f"  {simbolo:15} → Error: {str(e)[:40]}")
            
            # Pausa de 30 segundos
            print(f"\nPróxima actualización en 30 segundos...")
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n\nMonitoreo detenido por el usuario.")
    except Exception as e:
        print(f"Ocurrió un error general: {e}")

if __name__ == "__main__":
    # Lista de símbolos a monitorear
    simbolos = [
        "MSTR",      # MicroStrategy
        "F",         # Ford Motor Company
        "GM",        # General Motors
        "RIVN",      # Rivian
        "MARA",      # Marathon Digital Holdings
        "NVDA",      # NVIDIA
        "AMZN",      # Amazon
        "WMT",       # Walmart
        "^IXIC",     # NASDAQ Composite
        "^GSPC"      # S&P 500
    ]
    
    monitorear_acciones(simbolos)

