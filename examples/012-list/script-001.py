__author__ = 'Gaurav.Khanna'

data1=[1,2,3,4];

data2=['x','y','z'];

mixList = ['Gaurav',3,-3]

print(data1[0])
print(data1[0:2])
print(data2[-3:-1])
print(data1[0:])
print(data2[:2])

print(mixList) # List can have different type of data sets

list1=[10,20]
list2=[30,40]
list3=list1+list2
print(list3)

print('Number of Elements', data1.count(1)) # Count Number of Elements

print('Length of List :: ', len(data1)) # Length of List

data1.append(100)

print(data1)

data1.pop()

print(data1)

data1.clear()

print(data1)

data1.insert(1,89)

print(data1)