set_1 = {"apple", "apple", "apple", "banana", "banana"}
set_2 = set(["banana", "apple"])
set_3 = {"apple", "grapes"}

print(set_1 == set_2) # True

a = {1,2,3,4,5,6}
b = {2,3}
print(a.union(b)) # 1,2,3,4,5,6
print()
print(a.intersection(b)) # 2,3
print()
print(a.difference(b)) # 1,4,5,6