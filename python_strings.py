#check String we use "in" keyword
txt = 'I am Flutter developer'
print('am' in txt)
#by using condition
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)
#by using if condition
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")





#slicing  Strings

text = 'Hello, World!'
# from start of index to end of index
print(text[2:5])
# start from index 2  means 0,1
print(text[2:])
# except last 5 indexes 
print(text[:5])

#Negative indexing

#From: "o" in "World!" (position -5)To, but not included: "d" in "World!" (position -2):

print(text[-5:-2])




#Modify Strings
#UpperCase,LowerCase,strip,replace,split
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("H","J"))
print(text.split(","))





#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
#To add a space between them, add a " ":
c = a + " " + b
print(c)




#Format - Strings

#F-Strings
txt = "My name is "
name = "Ayan Javed"
print(f"{txt}{name}")

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Python Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Almost any value is evaluated to True if it has some sort of content.

#Any string is True, except empty strings.

#Any number is True, except 0.

#Any list, tuple, set, and dictionary are True, except empty ones.#


