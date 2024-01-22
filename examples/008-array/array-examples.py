from array import *

int_array = array('i',[1,3,5,7,9,10])

array_length = len(int_array)

for a in int_array:
    print("Element :: ", a)

print("Length of Array :: ", array_length)

for a in range(array_length):
    print("Element Range :: ", a+1)