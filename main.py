from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/SALUDVACUNASCOVIDV3/Dashboard1?:language=es&:display_count=y&publish=yes&:origin=viz_share_link&:embed=y&:showVizHome=n&:tabs=n&:toolbar=n&showShareOptions=false&:apiID=host0"

ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()

for t in workbook.worksheets:
    print(f"worksheet name: {t.name}") # show worksheet name
    print(t.data) # show dataframe for this worksheet

print("---------------")

ws = ts.getWorksheet("Graficos barras por edad")
print(ws.data)

print("---------------")

selections = ws.getSelectableItems()
print(selections)

print("---------------")

dashboard = ws.select("SUMA(Cobertura Pauta completa)", 0.3)

for t in dashboard.worksheets:
    print(t.data)