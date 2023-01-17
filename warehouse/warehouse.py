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

sold_items = []

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

def sell_item (item_name, quantity_to_sell):
    for item in items:
        if item_name == item ['name']:
            if item['quantity'] >= quantity_to_sell:
                item ['quantity'] = item ['quantity'] - quantity_to_sell
                return item
                sold_items.append ({'name' : item_name, 'quantity' : item ['quantity'] - quantity_to_sell, 'unit' :  item ['unit'], 'unit_price' : unit_price ['unit_price']})
            else:
                return None
    return None

def get_costs (items):
    costs = sum ((['quantity'] * item['unit_price']) for item in items)
    return costs

def get_income (sold_items):
    income = sum ((['quantity'] * item['unit_price']) for item in items)
    return income

def show_revenue (income, costs):
    print ("----------------")
    profit = income - costs
    return profit
        
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
            print ("Successfully sold %s %s of %s" % (quantity_to_sell, item ['unit'], item_name))
            print (get_items(items))
        else:
            print ('Sell unsuccessfull')
    elif decision == 'show_revenue':
        print (get_costs (items))
        print (get_income (sold_items))
        print (show_revenue (income, costs))
        if show_revenue < 0:
            print ("Revenue breakdown (PLN)")
   
    elif decision == 'exit':
        print = "Exiting... Bye!"
        break

    