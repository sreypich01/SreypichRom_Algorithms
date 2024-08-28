   
# EX10.Show product name that has maximum price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def sum(products):
    max=products[0]["price"]
    for i in range(len(products)):
        if products[i]["price"]>max:
                result=products[i]["name"] 
    return result

products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(sum(products))