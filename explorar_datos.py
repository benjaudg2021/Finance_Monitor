import yfinance as yf

print("="*100)
print("EXPLORANDO TODOS LOS DATOS DISPONIBLES DE UNA ACCIÓN")
print("="*100)

# 1. DATOS HISTÓRICOS
print("\n1️⃣  DATOS DE DESCARGA HISTÓRICA - yf.download()")
print("-"*100)
hist = yf.download("MSTR", period='5d', progress=False)
print(f"\nColumnas disponibles: {list(hist.columns)}")
print(f"Total de columnas: {len(hist.columns)}")

close_actual = hist['Close'].iloc[-1].item()
close_anterior = hist['Close'].iloc[-2].item()
open_val = hist['Open'].iloc[-1].item()
high_val = hist['High'].iloc[-1].item()
low_val = hist['Low'].iloc[-1].item()
volume_val = int(hist['Volume'].iloc[-1].item())

print(f"\n📊 Datos disponibles en cada fila histórica:")
print(f"  1. Close (Cierre):        ${close_actual:.2f}        ← Lo usamos")
print(f"  2. Open (Apertura):       ${open_val:.2f}")
print(f"  3. High (Máximo):         ${high_val:.2f}")
print(f"  4. Low (Mínimo):          ${low_val:.2f}")
print(f"  5. Volume (Volumen):      {volume_val:,} acciones")

# 2. INFORMACIÓN DETALLADA
print("\n\n2️⃣  INFORMACIÓN DETALLADA - yf.Ticker().info")
print("-"*100)
ticker = yf.Ticker("MSTR")
info = ticker.info

print(f"\nCantidad TOTAL de datos disponibles: {len(info)} campos\n")

# Mostrar datos organizados
print("📈 DATOS DE PRECIO Y VOLUMEN:")
print(f"  • currentPrice:        ${info.get('currentPrice', 'N/A')}")
print(f"  • dayHigh:             ${info.get('dayHigh', 'N/A')}")
print(f"  • dayLow:              ${info.get('dayLow', 'N/A')}")
print(f"  • volume:              {info.get('volume', 'N/A')} acciones")
print(f"  • averageVolume:       {info.get('averageVolume', 'N/A')} acciones")

print("\n📊 DATOS DE 52 SEMANAS:")
print(f"  • fiftyTwoWeekHigh:    ${info.get('fiftyTwoWeekHigh', 'N/A')}")
print(f"  • fiftyTwoWeekLow:     ${info.get('fiftyTwoWeekLow', 'N/A')}")

print("\n💰 CAPITALIZACIÓN Y ACCIONES:")
print(f"  • marketCap:           ${info.get('marketCap', 'N/A'):,.0f}" if info.get('marketCap') else "  • marketCap:           N/A")
print(f"  • sharesOutstanding:   {info.get('sharesOutstanding', 'N/A'):,}" if info.get('sharesOutstanding') else "  • sharesOutstanding:   N/A")

print("\n📈 RATIOS FINANCIEROS:")
print(f"  • trailingPE:          {info.get('trailingPE', 'N/A')}")
print(f"  • forwardPE:           {info.get('forwardPE', 'N/A')}")
print(f"  • priceToBook:         {info.get('priceToBook', 'N/A')}")
print(f"  • beta:                {info.get('beta', 'N/A')}")

print("\n💡 DIVIDENDOS:")
print(f"  • dividendRate:        {info.get('dividendRate', 'N/A')}")
print(f"  • yield:               {info.get('dividendYield', 'N/A')}")

print("\n🏢 INFORMACIÓN DE LA EMPRESA:")
print(f"  • sector:              {info.get('sector', 'N/A')}")
print(f"  • industry:            {info.get('industry', 'N/A')}")
print(f"  • employees:           {info.get('employees', 'N/A'):,}" if info.get('employees') else "  • employees:           N/A")
print(f"  • website:             {info.get('website', 'N/A')}")
print(f"  • country:             {info.get('country', 'N/A')}")

print("\n" + "="*100)
print(f"RESUMEN: 🎯 Actualmente usas 3 datos")
print(f"         📊 Disponibles {len(info)} campos para análisis adicional")
print("="*100)

# Información detallada (método .info)
print("\n\n2️⃣  INFORMACIÓN DETALLADA - yf.Ticker().info")
print("-"*100)
ticker = yf.Ticker("MSTR")
info = ticker.info

print(f"\nCantidad TOTAL de características disponibles: {len(info)} campos")
print(f"\nAlgunos campos importantes disponibles:")

campos_importantes = {
    "currentPrice": "Precio actual",
    "dayHigh": "Máximo del día",
    "dayLow": "Mínimo del día",
    "fiftyTwoWeekHigh": "Máximo de 52 semanas",
    "fiftyTwoWeekLow": "Mínimo de 52 semanas",
    "marketCap": "Capitalización de mercado",
    "volume": "Volumen del día",
    "trailingPE": "Ratio P/E (Price to Earnings)",
    "dividendRate": "Tasa de dividendo",
    "beta": "Beta (volatilidad vs mercado)",
    "debtToEquity": "Deuda/Patrimonio",
    "returnOnEquity": "ROE (Retorno sobre patrimonio)",
    "profitMargins": "Margen de ganancia",
    "operatingMargins": "Margen operativo",
    "priceToBook": "Precio/Libro",
    "forward Dividend Rate": "Dividendo a futuro",
    "employees": "Número de empleados",
    "website": "Sitio web",
    "sector": "Sector industrial",
    "industry": "Industria",
    "longBusinessSummary": "Descripción del negocio",
}

for campo, descripcion in campos_importantes.items():
    if campo in info:
        valor = info[campo]
        if isinstance(valor, (int, float)) and valor > 1000000:
            print(f"  ✓ {campo:25} ({descripcion:30}): {valor:,.0f}")
        else:
            print(f"  ✓ {campo:25} ({descripcion:30}): {valor}")
    else:
        print(f"  ✗ {campo:25} ({descripcion:30}): No disponible")

# Mostrar TODOS los campos disponibles
print("\n\n3️⃣  LISTA COMPLETA DE LOS 100+ CAMPOS DISPONIBLES EN .info")
print("-"*100)
print("\nCampos disponibles por categoría:\n")

categorias = {
    "PRECIO Y COTIZACIÓN": [k for k in info.keys() if any(x in k.lower() for x in ['price', 'current', 'bid', 'ask', 'target', 'trailing', 'forward', 'open', 'close', 'high', 'low'])],
    "VOLUMEN Y COMERCIO": [k for k in info.keys() if any(x in k.lower() for x in ['volume', 'average', 'bid', 'ask'])],
    "CAPITALIZACIÓN": [k for k in info.keys() if any(x in k.lower() for x in ['market', 'cap', 'shares', 'float'])],
    "VALUACIÓN": [k for k in info.keys() if any(x in k.lower() for x in ['pe', 'earnings', 'book', 'price/'])],
    "DIVIDEND": [k for k in info.keys() if any(x in k.lower() for x in ['dividend', 'yield', 'payout'])],
    "INFORMACIÓN FINANCIERA": [k for k in info.keys() if any(x in k.lower() for x in ['profit', 'margin', 'debt', 'equity', 'return', 'roe', 'roa'])],
    "DATOS DE EMPRESA": [k for k in info.keys() if any(x in k.lower() for x in ['sector', 'industry', 'website', 'employees', 'country', 'city'])],
    "DATOS HISTÓRICOS": [k for k in info.keys() if any(x in k.lower() for x in ['52week', 'fifty', 'year', 'month'])]
}

for categoria, campos in categorias.items():
    campos_validos = [c for c in campos if c in info and info[c] is not None]
    if campos_validos:
        print(f"\n{categoria}:")
        for campo in campos_validos:
            print(f"    • {campo}")

print(f"\n\nTOTAL DE CAMPOS EN .info: {len([k for k in info.keys() if info[k] is not None])} campos no vacíos")

print("\n" + "="*100)
print("RESUMEN: Actualmente solo usas 3 datos, pero hay 100+ campos disponibles para análisis")
print("="*100)

'''
====================================================================================================
EXPLORANDO TODOS LOS DATOS DISPONIBLES DE UNA ACCIÓN
====================================================================================================

1️⃣  DATOS DE DESCARGA HISTÓRICA - yf.download()
----------------------------------------------------------------------------------------------------

Columnas disponibles: [('Close', 'MSTR'), ('High', 'MSTR'), ('Low', 'MSTR'), ('Open', 'MSTR'), ('Volume', 'MSTR')]
Total de columnas: 5

📊 Datos disponibles en cada fila histórica:
  1. Close (Cierre):        $169.20        ← Lo usamos
  2. Open (Apertura):       $170.92
  3. High (Máximo):         $175.75
  4. Low (Mínimo):          $167.61
  5. Volume (Volumen):      13,171,350 acciones


2️⃣  INFORMACIÓN DETALLADA - yf.Ticker().info
----------------------------------------------------------------------------------------------------

Cantidad TOTAL de datos disponibles: 177 campos

📈 DATOS DE PRECIO Y VOLUMEN:
  • currentPrice:        $169.2
  • dayHigh:             $175.75
  • dayLow:              $167.61
  • volume:              13171350 acciones
  • averageVolume:       22192637 acciones

📊 DATOS DE 52 SEMANAS:
  • fiftyTwoWeekHigh:    $457.22
  • fiftyTwoWeekLow:     $104.17

💰 CAPITALIZACIÓN Y ACCIONES:
  • marketCap:           $59,285,454,848
  • sharesOutstanding:   330,746,592

📈 RATIOS FINANCIEROS:
  • trailingPE:          N/A
  • forwardPE:           4.650332
  • priceToBook:         1.1966646
  • beta:                3.56

💡 DIVIDENDOS:
  • dividendRate:        N/A
  • yield:               N/A

🏢 INFORMACIÓN DE LA EMPRESA:
  • sector:              Technology
  • industry:            Software - Application
  • employees:           N/A
  • website:             https://www.strategy.com
  • country:             United States

====================================================================================================
RESUMEN: 🎯 Actualmente usas 3 datos
         📊 Disponibles 177 campos para análisis adicional
====================================================================================================


2️⃣  INFORMACIÓN DETALLADA - yf.Ticker().info
----------------------------------------------------------------------------------------------------

Cantidad TOTAL de características disponibles: 177 campos

Algunos campos importantes disponibles:
  ✓ currentPrice              (Precio actual                 ): 169.2
  ✓ dayHigh                   (Máximo del día                ): 175.75
  ✓ dayLow                    (Mínimo del día                ): 167.61
  ✓ fiftyTwoWeekHigh          (Máximo de 52 semanas          ): 457.22
  ✓ fiftyTwoWeekLow           (Mínimo de 52 semanas          ): 104.17
  ✓ marketCap                 (Capitalización de mercado     ): 59,285,454,848
  ✓ volume                    (Volumen del día               ): 13,171,350
  ✗ trailingPE                (Ratio P/E (Price to Earnings) ): No disponible
  ✗ dividendRate              (Tasa de dividendo             ): No disponible
  ✓ beta                      (Beta (volatilidad vs mercado) ): 3.56
  ✓ debtToEquity              (Deuda/Patrimonio              ): 16.158
  ✓ returnOnEquity            (ROE (Retorno sobre patrimonio)): -0.111099996
  ✓ profitMargins             (Margen de ganancia            ): 0.0
  ✓ operatingMargins          (Margen operativo              ): -44.016068
  ✓ priceToBook               (Precio/Libro                  ): 1.1966646
  ✗ forward Dividend Rate     (Dividendo a futuro            ): No disponible
  ✗ employees                 (Número de empleados           ): No disponible
  ✓ website                   (Sitio web                     ): https://www.strategy.com
  ✓ sector                    (Sector industrial             ): Technology
  ✓ industry                  (Industria                     ): Software - Application
  ✓ longBusinessSummary       (Descripción del negocio       ): Strategy Inc, together with its subsidiaries, operates as a bitcoin treasury company in the United States, Europe, the Middle East, Africa, and internationally. It offers investors varying degrees of economic exposure to Bitcoin by offering a range of securities, including equity and fixed income instruments. The company also provides AI-powered enterprise analytics software, including Strategy One, which provides non-technical users with the ability to directly access novel and actionable insights for decision-making. In addition, the company provides Strategy Mosaic, a universal intelligence layer that offers enterprises with consistent definitions and governance across data sources, regardless of where that data resides or which tools access it. The company was formerly known as MicroStrategy Incorporated and changed its name to Strategy Inc in August 2025. The company was incorporated in 1989 and is headquartered in Tysons Corner, Virginia.


3️⃣  LISTA COMPLETA DE LOS 100+ CAMPOS DISPONIBLES EN .info
----------------------------------------------------------------------------------------------------

Campos disponibles por categoría:


PRECIO Y COTIZACIÓN:
    • priceHint
    • previousClose
    • open
    • dayLow
    • dayHigh
    • regularMarketPreviousClose
    • regularMarketOpen
    • regularMarketDayLow
    • regularMarketDayHigh
    • forwardPE
    • bid
    • ask
    • bidSize
    • askSize
    • fiftyTwoWeekLow
    • fiftyTwoWeekHigh
    • allTimeHigh
    • allTimeLow
    • priceToSalesTrailing12Months
    • trailingAnnualDividendRate
    • trailingAnnualDividendYield
    • priceToBook
    • trailingEps
    • forwardEps
    • currentPrice
    • targetHighPrice
    • targetLowPrice
    • targetMeanPrice
    • targetMedianPrice
    • currentRatio
    • freeCashflow
    • operatingCashflow
    • customPriceAlertConfidence
    • postMarketPrice
    • fiftyTwoWeekLowChange
    • fiftyTwoWeekLowChangePercent
    • fiftyTwoWeekHighChange
    • fiftyTwoWeekHighChangePercent
    • epsTrailingTwelveMonths
    • epsForward
    • epsCurrentYear
    • priceEpsCurrentYear
    • regularMarketPrice

VOLUMEN Y COMERCIO:
    • volume
    • regularMarketVolume
    • averageVolume
    • averageVolume10days
    • averageDailyVolume10Day
    • bid
    • ask
    • bidSize
    • askSize
    • fiftyDayAverage
    • twoHundredDayAverage
    • averageDailyVolume3Month
    • fiftyDayAverageChange
    • fiftyDayAverageChangePercent
    • twoHundredDayAverageChange
    • twoHundredDayAverageChangePercent
    • averageAnalystRating

CAPITALIZACIÓN:
    • regularMarketPreviousClose
    • regularMarketOpen
    • regularMarketDayLow
    • regularMarketDayHigh
    • regularMarketVolume
    • marketCap
    • nonDilutedMarketCap
    • floatShares
    • sharesOutstanding
    • sharesShort
    • sharesShortPriorMonth
    • sharesShortPreviousMonthDate
    • sharesPercentSharesOut
    • shortPercentOfFloat
    • impliedSharesOutstanding
    • hasPrePostMarketData
    • postMarketChangePercent
    • postMarketPrice
    • postMarketChange
    • regularMarketChange
    • regularMarketDayRange
    • regularMarketChangePercent
    • regularMarketPrice
    • market
    • postMarketTime
    • regularMarketTime
    • marketState

VALUACIÓN:
    • compensationRisk
    • compensationAsOfEpochDate
    • open
    • regularMarketOpen
    • forwardPE
    • sharesPercentSharesOut
    • heldPercentInsiders
    • heldPercentInstitutions
    • shortPercentOfFloat
    • bookValue
    • priceToBook
    • pegRatio
    • quoteType
    • totalCashPerShare
    • revenuePerShare
    • operatingCashflow
    • operatingMargins
    • typeDisp
    • postMarketChangePercent
    • fiftyTwoWeekLowChangePercent
    • fiftyTwoWeekHighChangePercent
    • fiftyTwoWeekChangePercent
    • earningsTimestamp
    • earningsTimestampStart
    • earningsTimestampEnd
    • earningsCallTimestampStart
    • earningsCallTimestampEnd
    • isEarningsDateEstimate
    • fiftyDayAverageChangePercent
    • twoHundredDayAverageChangePercent
    • regularMarketChangePercent

DIVIDEND:
    • payoutRatio
    • trailingAnnualDividendRate
    • trailingAnnualDividendYield
    • dividendDate

INFORMACIÓN FINANCIERA:
    • profitMargins
    • totalDebt
    • debtToEquity
    • returnOnAssets
    • returnOnEquity
    • grossProfits
    • grossMargins
    • ebitdaMargins
    • operatingMargins

DATOS DE EMPRESA:
    • city
    • country
    • website
    • industry
    • industryKey
    • industryDisp
    • sector
    • sectorKey
    • sectorDisp
    • fullTimeEmployees
    • irWebsite

DATOS HISTÓRICOS:
    • fiftyTwoWeekLow
    • fiftyTwoWeekHigh
    • priceToSalesTrailing12Months
    • fiftyDayAverage
    • sharesShortPriorMonth
    • sharesShortPreviousMonthDate
    • lastFiscalYearEnd
    • nextFiscalYearEnd
    • 52WeekChange
    • SandP52WeekChange
    • averageDailyVolume3Month
    • fiftyTwoWeekLowChange
    • fiftyTwoWeekLowChangePercent
    • fiftyTwoWeekRange
    • fiftyTwoWeekHighChange
    • fiftyTwoWeekHighChangePercent
    • fiftyTwoWeekChangePercent
    • epsTrailingTwelveMonths
    • epsCurrentYear
    • priceEpsCurrentYear
    • fiftyDayAverageChange
    • fiftyDayAverageChangePercent
'''