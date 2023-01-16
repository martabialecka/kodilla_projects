items = [
    {'name' :'chocolate',
    'quantity' : 200,
    'unit' : 'kg',
    "unit_price" : 4},
    {'name' :'sweets',
    'quantity' : 50,
    'unit' : 'kg',
    "unit_price" : 3},
    {'name' :'lollipop',
    'quantity' : 400,
    'unit' : 'kg',
    "unit_price" : 2}]

def get_items (items):
    # name:      15 
    # quantity:  12
    # unit:       8
    # unit_price: nvm
    table =  "Name           Quantity    Unit    Unit Price (PLN)\n"
    table += "____           ________    ____    __________\n"
    for item in items:
        table += \
            item['name'] + ' ' * (15 - len(item['name'])) + \
            str(item['quantity']) + ' ' * (12 - len(str(item['quantity']))) + \
            item['unit'] + ' ' * (8 - len(item['unit'])) + \
            str(item ['unit_price']) + '\n'

    return table

def add_item (n, q, u, up):
    items.append ({'name' : n, 'quantity' : q, 'unit' : u, 'unit_price' : up})


while True:
    decision = input ("What would you like to do? ")
    if decision == 'show':
        print (get_items(items))
    elif decision == 'add':
        print ("Adding to warehouse")
        name = input ("Item name: ")
        quantity = int(input ("Item quantity: "))
        unit = input ("Item unit of measure, f.ex. l, kg, pcs: ")
        unit_price = float(input ("Item price in PLN: "))
        add_item (name, quantity, unit, unit_price)  
    elif decision == 'exit':
        print = "Exiting... Bye!"
        break


