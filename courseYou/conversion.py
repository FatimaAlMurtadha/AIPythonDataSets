my_list = [1,2,3]
my_tuple = ("easy", "as")
my_set = {4,5,6}

print(list(my_tuple))
print(list(my_set))
print()

print(tuple(my_list))
print(tuple(my_set))
print()

print(set(my_list))
print(set(my_tuple))

l1 = [1,2,3,3,2,4,1]
l2 = [1,2,3,4]

print()
print(l1==l2) # false
print(set(l1) == set(l2)) # True

# ====================================
print("="*50)
t1 = (5,10,100,105,77)
t2 = (1,2,10, 101,105,100,44,23,25)
# print(t1.intersection(t2)) # ERROR
print()
print(set(t1).intersection(set(t2))) # 105,10,100

print("="*50)
print("="*50)
l = []
for r in range(0, 10, 2): 
    print(r) # 0, 2,4,6,8
    l.append(r*10) # [0, 20, 40, 60, 80]

print()
print(l) # [0, 20, 40, 60, 80]

print()

players = ["Ze", "be", "fe", "ee","oe"]

print("I'm the enumerate ")
print("We 2 are doing the same")
for iteration_number, i in enumerate(players):
    print(iteration_number, i)

print()
print("I'm the range")
for i in range(len(players)):
    print(i, players[i])

print()
for x in range(5):
    print()
    for j in range(x+1):
        print(f'{x}"{j} = ', x*j)







print()