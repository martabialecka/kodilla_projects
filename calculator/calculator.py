import sys
import logging

logging.basicConfig(level = logging.INFO)

dzialanie = int (input (("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")))
x = float (input ('Podaj liczbę 1. '))
y = float (input ('Podaj liczbę 2. '))
if dzialanie == 1:
    logging.info ("Dodaję %s i %s" % (x, y))
    result = x + y
elif dzialanie == 2:
    logging.info ("Odejmuję %s i %s" % (x, y))
    result = x - y
elif dzialanie == 3:
    logging.info ("Mnożę %s i %s" % (x, y))
    result = x * y
elif dzialanie == 4:
    logging.info ("Dzielę %s i %s" % (x, y))
    result = x / y

print ("Wynik to %s" % str (result))
