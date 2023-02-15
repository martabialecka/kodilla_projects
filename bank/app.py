import requests
import csv

if __name__ == '__main__':
    response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
    data = response.json()

    rates = data[0]['rates']

    with open('rates.csv', 'w', encoding = 'UTF-8', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ';')
        for row in rates:
            csvwriter.writerow([row['currency'], row['code'], row['bid'], row['ask']])

    exit(0)

from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import url_for

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
data = response.json()
rates_raw = data[0]['rates']

rates = {}

for row in rates_raw:
    rates[row['code']] = float(row['ask'])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bank():
    if request.method == 'GET':
        return render_template('bank.html', rates = rates, args = request.args)
    elif request.method == 'POST':
        try:
            currency = request.form['currency']
            amount = float(request.form['amount'])
            rate = rates[currency]
            price = rate * amount
            price = '%.4f' % price
        except:
            return redirect('/')
        return redirect(url_for('bank', currency = currency, amount = amount, rate = rate, price = price))
