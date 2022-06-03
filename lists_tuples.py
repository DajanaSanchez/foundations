customer_list = [
    'C00001', 'C00003', 'C00004', 'C00005', 'C00006',
    'C00007', 'C00018', 'C00010', 'C00013', 'C00014',
    'C00015', 'C00016', 'C00029'
]

print(customer_list)

if 'C00009' in customer_list:
    print(99.99)
else:
    print(0.0)

fifth_sixth = customer_list[4:6]

fifth_sixth

every_third = customer_list[::3]

every_third

last_two = customer_list[-2:]

last_two



#calculate sales tax for customer with 3 purchases
multi_order_customers = [
    [1799.94, 29.98, 99.99],
    [15.98, 119.99],
    [24.99, 24.99],
    [649.99, 99.99],
    [599.99, 399.97]
]

tuple(multi_order_customers)

transaction1, transaction2, transaction3 = tuple(multi_order_customers[0])

print(round(transaction1 * .08, 2))
print(round(transaction2 * .08, 2))
print(round(transaction3 * .08, 2))


#update customer list

customer_list = [
    'C00001', 'C00003', 'C00004','C00005', 'C00006',
    'C00007', 'C00008', 'C00010', 'C00013', 'C00014',
    'C00015', 'C00016', 'C00020'
]

customer_list.insert(7, 'C00009')
print(customer_list)


saturday_list = [
    'C00004', 'C00017', 'C00019', 'C00002', 'C00008',
    'C00021', 'C00022'
]

customer_list = (customer_list + saturday_list)
print(customer_list)