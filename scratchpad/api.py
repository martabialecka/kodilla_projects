import requests

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/a/2023-02-13/")
data = response.json()
print (data)

rates = [data]

import csv
with open('rates.csv', 'w', encoding = 'UTF-8') as csvfile:
    csvwriter = csv.writer (csvfile)
    csvwriter = write.row ("currency";"code";"bid";"ask")

 