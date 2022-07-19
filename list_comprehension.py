#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. 
#Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#syntax: newList = [ expression(gives the element) for element in oldList if condition ] 

#A list till containing numbers from 1 to 10
print([x for x in range(1,11)])

fruits = ["apple","banana","mango","kiwi"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Example 2: Even list using list comprehension
print([x for x in range (1,25) if x%2==0])

#Find all of the numbers from 1–1000 that are divisible by 8
num_8 = [x for x in range(1,1000) if x%8==0]
#print(num_8)

#Find all of the numbers from 1–1000 that have a 6 in them
num_6 = [x for x in range(1,1000) if "6" in str(x)]
#print(num_6)

#Count the number of spaces in a string
string = "Practice Problems to Drill List Comprehension in Your Head."
spaces = [x for x in string if " " in (x)]
print(len(spaces))

#Remove all of the vowels in a string
new = "".join([x for x in string if x not in  ["a","e","i","o","u"]])
print(new)

#Find all of the words in a string that are less than 5 letters
words = string.split()
print(words)

a = [word for word in words if len(word)< 5]
print(a)



