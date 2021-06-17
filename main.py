from tableauscraper import TableauScraper as TS
import private
from bot_functions import startBot

# Obtain keys from private.py
api = startBot(private.consumer_key, private.consumer_secret_key, private.access_token, private.access_token_secret)

url = "https://public.tableau.com/views/SALUDVACUNASCOVIDV3/Dashboard1"

ts = TS()
ts.loads(url)

# Get title sheet to obtain date
dateSheet = ts.getWorksheet("Titulo D3")
dateSelection = dateSheet.getSelectableItems()

for i in dateSelection:
    if i.get('column') == 'DAY(Fecha)':
        date = i.get('values')[-1]

# Get main sheet to obtain data from Córdoba
mainSheet = ts.getWorksheet("Graficos barras por edad")
cordobaSheet = mainSheet.setFilter('Territorio', 'Córdoba')
cordobaData = cordobaSheet.getWorksheet("Graficos barras por edad")

cordobaSelection = cordobaData.getSelectableItems()

# Find value of "Pauta completa"
for i in cordobaSelection:
    if i.get('column') == 'SUM(Pauta completa)':
        pauta_completa = i.get('values')[-1]
        continue
    
    if i.get('column') == 'SUM(Cobertura Pauta completa)':
        cobertura_pauta_completa = i.get('values')[-1]
        continue

print(f"Dato de vacunaciones en córdoba: {pauta_completa} ({cobertura_pauta_completa}%). Fecha: {date}")