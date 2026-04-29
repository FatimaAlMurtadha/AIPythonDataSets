from directory.module import my_awesome_function
from flowers.roses import list_roses
from classes.my_class import MyClass

my_roses = list_roses()
print()

my_awesome_function()

c1 = MyClass(1)
c2 = MyClass(2)

print(c1.value)


print(c1.value)
print(c2.value)

def add1(items):
    items.append("!")

xs = ["hello"]
add1(xs)
print(xs)

def add2(s):  
  s += "!"
  return s

greeting = "hello"
add2(greeting)
print(greeting)

greetings2 = add2(greeting)
print(greetings2)

def append_to(item, target=[]):
    target.append(item)
    return target

print(append_to(1)) # [1]
print(append_to(2)) # [1, 2] - the list is shared between calls, which can lead to unexpected behavior

