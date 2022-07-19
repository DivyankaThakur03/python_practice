#Write a program for the implementation of the methods of a dictionary

dict= {}

n = int(input("Enter the number of items you want in the diictionary : "))

for _ in range(n):
    text = input("Enter key and value :").split()
    dict[text[0]] = text[1]
print("The dictionary is -",dict)

select =int(input('''Select which method to be performed on the dictionary - 
1- Adding an item
2- Deleting an item
3- Finding the length of the dictionary 
Selected option is :'''))

if select ==1:
    text = input("Enter key and value that you want to add : ").split()
    dict[text[0]] = text[1]
    print(dict)

elif select ==2:
    n = input("Enter the key that you want to delete :")
    del dict[n]
    print(dict)

elif select ==3:
    print("The length of the dictionary is", len(dict))

else:
    print("The selected option is not present.Do try the other option's!!!")

print("You can implement different method's too :) \n Love you Rajesh!!!")