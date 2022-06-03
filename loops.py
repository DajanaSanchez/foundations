#apply sales tax to all of the transactions/ calculate the the total invoice value
subtotals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99, 24.99, 1799.94, 99.99]

taxes = []
totals = []

for tax in subtotals:
     taxes.append(round(tax * .08, 2))

print(taxes)

taxes = []
totals = []

for subtotal in subtotals:
    total = round(subtotal + tax, 2)
    totals.append(total)

print(totals)

output_sum = []
for i in range(0,len(subtotals)):
    total_sum = round(subtotals[i] + taxes[i], 2)
    output_sum.append(total_sum)
print(output_sum)

for i in range(0, len(subtotals)):
    print(i)


#need to modify loop to take different sales tax rates into consideration

location = [
    'Sun Valley', 'Stowe', 'Mammoth', 'Stowe', 'Sun Valley',
    'Mammoth', 'Mammoth', 'Mammoth', 'Sun Valley'
]

updated_totals = []
taxes = []

for i, subtotal in enumerate(subtotals):
    if location[i] == 'Sun Valley':
        tax = round(subtotal * .08 ,2)
    elif location[i] == 'Stowe':
        tax = round(subtotal * .06, 2)
    else:
        tax = round(subtotal * .0775, 2)
    total = round(subtotal + tax, 2)
    taxes.append(tax)
    updated_totals.append(total)

print(updated_totals)
print(taxes)

#need to apply a 10% discount to every transaction

orders_c00001 = [1799.94, 29.98, 99.99]
orders_c00004 = [15.98, 119.99]
orders_c00006 = [24.99, 24.99]
orders_c00008 = [649.99, 99.99]
orders_c00010 = [599.99, 399.97]

multi_order_customers = [
    [1799.94, 29.98, 99.99],
    [15.98, 119.99],
    [24.99, 24.99],
    [649.99, 99.99],
    [599.99, 399.97]
]

multi_order_customers

discounted_prices = []

for customer in multi_order_customers:
    customer_discounts = []
    for transaction in customer:
        customer_discounts.append(round(transaction *.9,2))
    discounted_prices.append(customer_discounts)

discounted_prices

#inventory status

items = ['skis', 'snowboard', 'goggles', 'boots']
inventory = [10, 0, 0, 7]

inventory_status = {}

for i, item in enumerate(items):
    if inventory[i] == 0:
        inventory_status[item] = 'Sold Out'
    else:
        inventory_status[item] = 'In Stock'

        inventory_status

#inventory projections

current_inventory = 686
monthly_sales = 84
month = 0

while current_inventory > 0:
    current_inventory -= monthly_sales
    month += 1
    print(f' At the end of month {month} ,our inventory is {current_inventory}')

#affordability calculator

price_list = [5.99, None, 19.99, 24.99, 0, '74.99', 99.99]
budget = 100

# loop to calculate how many of each item I can buy
for price in price_list:
    if price == None:
        continue
    try:
        affordable_quantity = budget//float(price)
        print(f"I can buy {affordable_quantity} of these.")
    except ZeroDivisionError:
        print("This product is free, I can take as many as I like.")
    except TypeError:
        affordable_quantity = budget//float(price)
        print(f"I can buy {affordable_quantity} of these.")
    except:
        print('this was string data')