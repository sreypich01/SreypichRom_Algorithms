# EX1.Create function to sum numbers in array [1,2,3,4,5,6]
# def sum(array):
#     sum=0
#     for i in range(len(array)):
#         sum+=array[i]
#     return sum

# print(sum([1,2,3,4,5,6]))
# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
# def sum(array):
#     sum_odd=0
#     for i in range(len(array)):
#         if array[i]%2==1:
#             sum_odd+=array[i]
#     return sum_odd

# print(sum([1,2,3,4,5,6]))
# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
# def number(array):
#     max=array[0]
#     for i in range(len(array)):
#         if array[i]>max:
#             max=array[i]
#     return max

# print(number([2,3,5,0,11,5,2]))
# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]
# def number(array):
#     min=array[0]
#     for i in range(len(array)):
#         if array[i]<min:
#             min=array[i]
#     return min

# print(number([2,3,5,0,11,5,2]))
# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]
# def number(array):
#     count=0
#     for i in range(len(array)):
#         if array[i]==5:
#             count+=1
#     return count

# print(number([2,3,5,0,11,5,2]))
# EX6.Create function to count positive number in array [-1,11,2,0,-1,4]
# def number(array):
#     count=0
#     for i in range(len(array)):
#         if array[i]>0:
#             count+=1
#     return count

# print(number([-1,11,2,0,-1,4]))
# EX7.Create function to count negative number in array [-1,11,2,0,-1,4]
# def number(array):
#     count=0
#     for i in range(len(array)):
#         if array[i]<0:
#             count+=1
#     return count

# print(number([-1,11,2,0,-1,4]))
# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
# def sum(products):
#     total=0
#     for i in range(len(products)):
#         total+=products[i]["price"]
#     return total

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
# print(sum(products))    
# EX9.Create function to find average of price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
# def sum(products):
#     average=0
#     for i in range(len(products)):
#         average+=products[i]["price"]/len(products)
#     return average

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
# print(sum(products))    
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