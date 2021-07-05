from bot_functions import startBot, createProgressBar, updateProgressBar, getDateScructure, isNewData
from tableauscraper import TableauScraper as TS

# Obtain keys from private.py
api = startBot()

# Create progress bar for the first time
# createProgressBar()

# Obtain the data
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

# Find value of "Al menos 1D" and "Pauta completa"
for i in cordobaSelection:
    if i.get('column') == 'SUM(Al menos 1D)':
        al_menos_1D = i.get('values')[-1]
        continue
    
    if i.get('column') == 'SUM(Cobertura 1D)':
        cobertura_al_menos_1D = i.get('values')[-1]
        continue

    if i.get('column') == 'SUM(Pauta completa)':
        pauta_completa = i.get('values')[-1]
        continue
    
    if i.get('column') == 'SUM(Cobertura Pauta completa)':
        cobertura_pauta_completa = i.get('values')[-1]
        continue

# Check if the data has changed
print_info = f"Dato de vacunaciones en Córdoba, España (Fecha: {date}):\n - Al menos una dosis: {al_menos_1D} personas ({cobertura_al_menos_1D}%).\n - Pauta completa: {pauta_completa} personas ({cobertura_pauta_completa}%)."
if isNewData(api, print_info):
    # Update image using percentages
    updateProgressBar(cobertura_al_menos_1D, cobertura_pauta_completa, date)

    # Create tweet
    dt = getDateScructure(date)
    api.update_with_media(f"../images/{dt.year}-{dt.month}-{dt.day}.jpg", print_info);
    print(print_info)

else:
    print("No hay nuevos datos")