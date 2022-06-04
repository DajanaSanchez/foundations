#function that takes sub-total, tax rate and returns total amount

def tax_calculator(sub_total, tax_rate):
    tax = sub_total * tax_rate
    total = sub_total + tax
    return total

#apply tax calculator to sub_totals below and combine with customer Ids

sub_totals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99]
customer_ids = ['C00004', 'C00007', 'C00015', 'C00016', 'C00020', 'C00010']

full_transaction = []

for sub_t in sub_totals:
    full_transaction.append(tax_calculator(sub_t))

full_transaction

customer_dict = dict(zip(customer_ids, full_transaction))

customer_dict

#mapping tax calculator

subtotals = [1799.94, 99.99, 254.95, 29.98, 99.99]

import tax_calculator as tc

map(tc.tax_calculator, subtotals)

list(map(tc.tax_calculator, subtotals))

#apply discount to orders over $500

subtotals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99]

discounted_subtotals =
list(
    map(
        lambda x: round(x - (x * .10), 2) if x > 500 else x, subtotals)
)

discounted_subtotals

#modify tax calculator to have default tax rate of 6%

%%writefile tax_calculator.py

def tax_calculator(sub_total, tax = .06):
    totals = sub_total + np.round((sub_total * tax)
    return [sub_total, tax, totals]


#function that calls on tax calculator on list of subtotals then returns a dictionary

from tax_calculator import tax_calculator

customer_ids = ['C00004', 'C00007', 'C00015', 'C00016', 'C00020', 'C00010']

subtotals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99]

def trans_dict_creator(customer_ids, subtotals, tax_rate):
    customer_dict = {
        customer_id: tax_calculator(subtotals, tax_rate)
        for customer_id, subtotals in zip(customer_ids, subtotals)
    }
    return customer_dict

trans_dict_creator(customer_ids, subtotals, .08)
