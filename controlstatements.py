temperature = 15

if temperature > 25:
    print("it is too hot")
else:
    print("it is too cold")

# A python program that checks three numbers and displays the smallest
    num1 = int(input("enter the value of num1: "))
    num2 = int(input("enter the value of num2: "))
    num3 = int(input("enter the value of num3: "))

    if num1 < num2 and num1 < num3:
        print(num1,"is the smallest number")
    elif num2 < num1 and num2 < num3:
        print(num2,"is the smallest number")
    else:
        print(num3,"is the smallest number")

    # A python program that checks three numbers and displays the greatest
    x = 50
    y = 26
    z = 38

    if x > y and x > z:
        print(x,"is the greatest number")
    elif y > x and y > z:
        print(y,"is the greatest number")
    else:
        print(z,"is the greatest number")
