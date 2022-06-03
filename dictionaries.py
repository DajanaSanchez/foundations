#create dictionary for european items

item_ids = [
    10001, 10002, 10003, 10004, 10005,
    10006, 10007, 10008, 10009
]

item_names = [
    "Coffee", "Beanie", "Gloves", "Sweatshirt", "Helmet",
    "Snow Pants", "Coat", "Ski Poles", "Ski Boots"
]

euro_prices = [
    5.27, 8.79, 17.59, 21.99, 87.99,
    70.39, 105.59, 87.99, 175.99
]

item_category = [
    "beverage", "clothing", "clothing", "clothing", "safety",
    "clothing", "clothing", "hardware", "hardware",
]

sizes = [
    ["250mL"],
    ["Child", "Adult"],
    ["Child", "Adult"],
    ["XS", "S", "M", "L", "XL", "XXL"],
    ["Child", "Adult"],
    ["XS", "S", "M", "L", "XL", "XXL"],
    ["S", "M", "L"],
    ["S", "M", "L"],
    [5, 6, 7, 8, 9, 10, 11],
]

zip(item_ids)
zip(item_names, euro_prices, item_category, sizes)

list(zip(item_names, euro_prices, item_category, sizes))

euro_dict = dict(zip(item_ids, zip(item_names, euro_prices, item_category, sizes)))



#find size counts


item_dict = {
    10001: ('Coffee', 5.99, 'beverage', ['250mL']),
    10002: ('Beanie', 9.99, 'clothing', ['Child', 'Adult']),
    10003: ('Gloves', 19.99, 'clothing', ['Child', 'Adult']),
    10004: ('Sweatshirt', 24.99, 'clothing', ['XS', 'S', 'M', 'L', 'XL', 'XXL']),
    10005: ('Helmet', 99.99, 'safety', ['Child', 'Adult']),
    10006: ('Snow Pants', 79.99, 'clothing', ['XS', 'S', 'M', 'L', 'XL', 'XXL']),
    10007: ('Coat', 119.99, 'clothing', ['S', 'M', 'L']),
    10008: ('Ski Poles', 99.99, 'hardware', ['S', 'M', 'L']),
    10009: ('Ski Boots', 199.99, 'hardware', [5, 6, 7, 8, 9, 10, 11])
}

size_counts = {}

for key, value in item_dict.items():
    size_counts[key] = len(value[3])

size_counts

new_size_counts = {10010: '4', 10011: '7'}
size_counts.update(new_size_counts)

size_counts

exchange_rate = .88
euro_prices = []

for value in item_dict.values():
    euro_prices.append(round(value[1] * exchange_rate,2))


euro_prices