# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
def number(array):
    max=array[0]
    for i in range(len(array)):
        if array[i]>max:
            max=array[i]
    return max

print(number([2,3,5,0,11,5,2]))