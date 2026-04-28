'''
Goal del development es tener una interfaz grafica que obetenga el valor de la accion listada y poder visualizarla en tiempo real con un refresque elegido:
cada 5 segundos, 15, 30, 60, 5 min, 10, 15, etc.
Ademas de la lsita de acciones, y seteo del refresque de info, la app sera capaz de notificar ciertos casos, como cuando la accion alcance cierto valor
Interfaz grafica dirigida a Samsung Galaxy watch 6 classic
'''


import yfinance as yf
import time
from datetime import datetime

# Diccionario con nombres completos de las acciones
NOMBRES_ACCIONES = {
    "MSTR": "MicroStrategy",
    "F": "Ford Motor Company",
    "GM": "General Motors",
    "RIVN": "Rivian",
    "MARA": "Marathon Digital Holdings",
    "NVDA": "NVIDIA",
    "AMZN": "Amazon",
    "WMT": "Walmart",
    "^IXIC": "NASDAQ Composite",
    "^GSPC": "S&P 500"
}

def obtener_precio(simbolo):
    """
    Obtiene el precio actual de un símbolo.
    Retorna (precio, cambio, cambio_porcentaje) o (None, None, None) si falla.
    """
    try:
        hist = yf.download(simbolo, period='5d', progress=False)
        
        if hist is None or len(hist) == 0:
            return None, None, None
        
        # Obtener el último cierre
        try:
            precio_actual = hist['Close'].iloc[-1].item()
        except:
            precio_actual = hist['Close'].iloc[-1]
        
        # Validar que es un número válido
        if precio_actual is None or precio_actual != precio_actual:
            return None, None, None
        
        precio_actual = float(precio_actual)
        
        # Calcular cambio
        if len(hist) >= 2:
            try:
                cierre_anterior = hist['Close'].iloc[-2].item()
            except:
                cierre_anterior = hist['Close'].iloc[-2]
            
            cierre_anterior = float(cierre_anterior)
            cambio = precio_actual - cierre_anterior
            cambio_pct = (cambio / cierre_anterior * 100) if cierre_anterior != 0 else 0
        else:
            cambio = 0
            cambio_pct = 0
        
        return precio_actual, cambio, cambio_pct
        
    except Exception as e:
        return None, None, None

def monitorear_acciones(simbolos):
    """
    Monitorea múltiples acciones e índices simultáneamente.
    
    Args:
        simbolos (list): Lista de símbolos a monitorear
    """
    print(f"--- Iniciando monitoreo de {len(simbolos)} activos ---\n")
    
    try:
        while True:
            ahora = datetime.now().strftime("%H:%M:%S")
            print(f"\n{'='*80}")
            print(f"[{ahora}] ACTUALIZACIÓN DE PRECIOS")
            print(f"{'='*80}")
            
            for simbolo in simbolos:
                nombre_completo = NOMBRES_ACCIONES.get(simbolo, simbolo)
                precio, cambio, cambio_pct = obtener_precio(simbolo)
                
                if precio is not None:
                    print(f"  {simbolo:10} {nombre_completo:30} → ${precio:10.2f}", end="")
                    if cambio is not None and cambio_pct is not None:
                        signo = "+" if cambio >= 0 else ""
                        print(f"  ({signo}{cambio:7.2f} | {signo}{cambio_pct:6.2f}%)")
                    else:
                        print()
                else:
                    print(f"  {simbolo:10} {nombre_completo:30} → ⚠️ No disponible")
            
            print(f"\nPróxima actualización en 30 segundos...")
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n\nMonitoreo detenido por el usuario.")
    except Exception as e:
        print(f"Error: {e}")

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

