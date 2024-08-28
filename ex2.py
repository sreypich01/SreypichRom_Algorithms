# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sum(array):
    sum_odd=0
    for i in range(len(array)):
        if array[i]%2==1:
            sum_odd+=array[i]
    return sum_odd

print(sum([1,2,3,4,5,6]))