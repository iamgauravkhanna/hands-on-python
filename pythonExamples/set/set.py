__author__ = 'Gaurav.Khanna'

# Set is immutable and don't maintains order and don't store duplicate value

setObj = {1,3,5}

print(setObj)

# Same as {"a", "b","c"}
normal_set = set(["a", "b", "c"])

# Adding an element to normal set is fine
normal_set.add("d")

print("Normal Set")

print(normal_set)

normal_set.add("d")

print(normal_set)