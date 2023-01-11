import logging

logging.basicConfig(level = logging.INFO)

operation = int (input (("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")))
x = float (input ('Podaj liczbę 1. '))
y = float (input ('Podaj liczbę 2. '))
if operation == 1:
    logging.info ("Dodaję %s i %s" % (x, y))
    result = x + y
elif operation == 2:
    logging.info ("Odejmuję %s i %s" % (x, y))
    result = x - y
elif operation == 3:
    logging.info ("Mnożę %s i %s" % (x, y))
    result = x * y
elif operation == 4:
    logging.info ("Dzielę %s i %s" % (x, y))
    result = x / y

print ("Wynik to %s" % str (result))
