from tableauscraper import TableauScraper as TS
from private import consumer_key, consumer_secret_key, access_token, access_token_secret
from bot_functions import startBot, progressBar
from PIL import ImageColor

# Obtain keys from private.py
api = startBot(consumer_key, consumer_secret_key, access_token, access_token_secret)

progressBar()

# url = "https://public.tableau.com/views/SALUDVACUNASCOVIDV3/Dashboard1"

# ts = TS()
# ts.loads(url)

# # Get title sheet to obtain date
# dateSheet = ts.getWorksheet("Titulo D3")
# dateSelection = dateSheet.getSelectableItems()

# for i in dateSelection:
#     if i.get('column') == 'DAY(Fecha)':
#         date = i.get('values')[-1]

# # Get main sheet to obtain data from Córdoba
# mainSheet = ts.getWorksheet("Graficos barras por edad")
# cordobaSheet = mainSheet.setFilter('Territorio', 'Córdoba')
# cordobaData = cordobaSheet.getWorksheet("Graficos barras por edad")

# cordobaSelection = cordobaData.getSelectableItems()

# # Find value of "Pauta completa"
# for i in cordobaSelection:
#     if i.get('column') == 'SUM(Pauta completa)':
#         pauta_completa = i.get('values')[-1]
#         continue
    
#     if i.get('column') == 'SUM(Cobertura Pauta completa)':
#         cobertura_pauta_completa = i.get('values')[-1]
#         continue

# print(f"Dato de vacunaciones en córdoba (pauta completa): {pauta_completa} ({cobertura_pauta_completa}%). Fecha: {date}")
# api.update_status(f"Dato de vacunaciones en córdoba (pauta completa): {pauta_completa} ({cobertura_pauta_completa}%). Fecha: {date}");