
# EX9.Create function to find average of price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def sum(products):
    average=0
    for i in range(len(products)):
        average+=products[i]["price"]/len(products)
    return average

products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(sum(products)) 