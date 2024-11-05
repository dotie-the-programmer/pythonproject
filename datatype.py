
number = 56 #Integer
second = 43.12 #Float
greeting = "hello there" #String
isPythonIntresting = True #Boolean

#Data structures- Multiple values stored in a single variable
cars = ["toyota","nissan","vw"] #List - Ordered and changeable
fruits = ("banana","orange","apple") #Tuple -Ordered but unchangeable
countries = {"Kenya","Tunisia","Algeria"} #Set -Unordered
student = {
    "firstname" : "Dorothy",
    "age" : 23,
    "course" : "web Development",
    "nationality" : "kenyan"
} #Dictionary -key-value pair



print(cars)
print(fruits)
print(countries)
print(student)
print(student["course"])

print(number)
print(second)
print(isPythonIntresting)

#Determining a datatype
print(type(student))
print(type(countries))

#Typecasting - Converting one datatype into another
print(float(number))
print(int(second))