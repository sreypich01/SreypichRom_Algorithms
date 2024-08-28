# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]
def number(array):
    min=array[0]
    for i in range(len(array)):
        if array[i]<min:
            min=array[i]
    return min

print(number([2,3,5,0,11,5,2]))