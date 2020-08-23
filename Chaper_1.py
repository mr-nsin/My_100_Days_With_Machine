# This program says hello and asks for my name and show my age.
print('Hello, World!')

print('What is your name?') #ask for name

myName = input()

print('It is good to meet you ' + myName)

print('The length of your name is :')
print(len(myName))

print('Please tell your age:') # ask for age
myAge = input()
print('You will be ' + str(int(myAge) + 1)+ ' in a year.')