#built-in functions

y = max(34, 56, 70, 18)
print(y)

x = min(40, 67, 34, 25)
print(x)

z = pow(2, 3)
print("the result is",z)

#User-defined functions
def greeting():
    print("hello there!")

greeting() #calling function

def multiply():
    a = 12
    b = 10
    print(a * b)

multiply()

#Parameters/variable and Argument/value
def add():
    x = 4
    y = 5
    print(x + y)

add()

def add(x, y):
    print(x + y)

add(4, 5)
add(60, 70)

def employee(fullname,age,position,status):
    print(fullname,age,position,status)

employee("nick big", 45, "ceo",  "married")
employee("mark joe", 54, "clerk",  "single")
employee("rose vun", 56, "manager",  "married")
employee("marek jo", 34, "receptionist",  "single")