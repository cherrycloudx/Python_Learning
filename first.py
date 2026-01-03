name = input("What is your name? ")
age = input("What is your age ")
# For multiple lines use multiple print()
"""print("Hello", name)
print("You are", age, "years old. ")
"""
#For single line output use single print()
"""print("Hello", name , " you are", age, "years old")"""
#Use end='\n'
#after end only one string is allowed
#wrong: print("Hello", name , end= '\n' + " you are", age, "years old")
#right way:
print("Hello", name , end= '\n')
print("You are", age, "years old")




