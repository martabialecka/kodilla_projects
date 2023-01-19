import csv
import sys

items = [
    {'name' :'chocolate',
    'quantity' : 200,
    'unit' : 'kg',
    "unit_price" : 4.0},
    {'name' :'sweets',
    'quantity' : 50,
    'unit' : 'kg',
    "unit_price" : 3.0},
    {'name' :'lollipop',
    'quantity' : 400,
    'unit' : 'kg',
    "unit_price" : 2.0}]

sold_items = []

def get_items (items):
    # name:      15 
    # quantity:  12
    # unit:       8
    # unit_price: nvm
    table =  "Name           Quantity    Unit    Unit Price (PLN)\n"
    table += "____           ________    ____    __________\n"
    for item in items:
        unit_price_string = "%.2f" % item ['unit_price']
        table += \
            item['name'] + ' ' * (15 - len(item['name'])) + \
            str(item['quantity']) + ' ' * (12 - len(str(item['quantity']))) + \
            item['unit'] + ' ' * (8 - len(item['unit'])) + \
            unit_price_string + '\n'

    return table

def add_item (name, quantity, unit, unit_price):
    items.append ({'name' : name, 'quantity' : quantity, 'unit' : unit, 'unit_price' : unit_price})

def sell_item (item_name, quantity_to_sell):
    for item in items:
        if item_name == item ['name']:
            if item['quantity'] >= quantity_to_sell:
                item ['quantity'] = item ['quantity'] - quantity_to_sell
                sold_items.append ({'name' : item_name, 'quantity' : quantity_to_sell, 'unit' :  item ['unit'], 'unit_price' : item ['unit_price']})
                return item
            else:
                return None
    return None

def get_costs (items):
    costs = sum ([(item['quantity'] * item['unit_price']) for item in items])
    return costs

def get_income (sold_items):
    income = sum ([(item['quantity'] * item['unit_price']) for item in sold_items])
    return income

def show_revenue (items, sold_items):
    income = get_income (sold_items)
    costs = get_costs (items)
    profit = income - costs
    return (income, costs, profit)

def export_items_to_csv (items):
    with open ('magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in items:
            writer.writerow (item)

def load_items_from_csv(items, file):
    list.clear(items)
    with open(file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for item in reader:
            item ['unit_price'] = float(item ['unit_price'])
            items.append(item)

if len(sys.argv) > 1:
    load_items_from_csv (items, sys.argv [1])
    print ("Successfully loaded data from %s" % sys.argv[1])


while True:
    decision = input ("What would you like to do? ")
    if decision == 'show':
        print (get_items(items))
    elif decision == 'add':
        print ("Adding to warehouse...")
        name = input ("Item name: ")
        quantity = int(input ("Item quantity: "))
        unit = input ("Item unit of measure, f.ex. l, kg, pcs: ")
        unit_price = float(input ("Item price in PLN: "))
        add_item (name, quantity, unit, unit_price)
    elif decision == 'sell':
        item_name = input ("Item name: ")
        quantity_to_sell = int(input ("Quantity to sell: "))
        item = sell_item (item_name, quantity_to_sell)
        if item:
            print ("Successfully sold %d %s of %s" % (quantity_to_sell, item ['unit'], item_name))
            print (get_items(items))
        else:
            print ('Sell unsuccessfull')
    elif decision == 'show_revenue':
        (income, costs, profit) = show_revenue (items, sold_items)
        print ("Revenue breakdown (PLN)")
        print ("Income: %.2f" % income)
        print ("Costs: %.2f" %  costs)
        print ("-------------")
        print ("Revenue: %.2f PLN" % profit)
    elif decision == 'save':
        print ('Successfully saved data to magazyn.csv')
        export_items_to_csv(items)
    elif decision == 'load':
        print ('Successfully loaded data from magazyn.csv')
        load_items_from_csv(items, 'magazyn.csv')
    elif decision == 'exit':
        print = "Exiting... Bye!"
        break


