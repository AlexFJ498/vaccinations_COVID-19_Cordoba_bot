from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/SALUDVACUNASCOVIDV3/Dashboard1"

ts = TS()
ts.loads(url)
ws = ts.getWorksheet("Graficos barras por edad")

wss = ts.getWorksheet("Titulo D3")
wbselections = wss.getSelectableItems()

for i in wbselections:
    if i.get('column') == 'DAY(Fecha)':
        date = i.get('values')[-1]

# Get data from Córdoba
cordoba_wb = ws.setFilter('Territorio', 'Córdoba')
cordoba_ws = cordoba_wb.getWorksheet("Graficos barras por edad")

selections = cordoba_ws.getSelectableItems()

# Find value of "Pauta completa"
for i in selections:
    if i.get('column') == 'SUM(Pauta completa)':
        pauta_completa = i.get('values')[-1]
        continue
    
    if i.get('column') == 'SUM(Cobertura Pauta completa)':
        cobertura_pauta_completa = i.get('values')[-1]
        continue

print(f"Dato de vacunaciones en córdoba: {pauta_completa} ({cobertura_pauta_completa}%). Fecha: {date}")