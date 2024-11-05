courses = ["MIT","datascience","cybersecurity"]
print(courses)

#Accessing an element in array
print(courses[1])

#looping through an array
for y in courses:
    print("course is",y)

#Adding a new element
courses.append("Android Development")
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)