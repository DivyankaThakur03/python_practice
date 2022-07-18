# write a program having the methods of a list
list = []
l = int(input("Enter the number of element's in your list : "))
print("The {} number's of your list are : ".format(l))

for i in range(0,l):
    n = int(input())
    list.append(n)
print("The list is:",list)


select =int(input('''Select which method to be performed on the list - 
1-append
2-insert
3-remove
4-pop
5-index
6-count
7-sort 
8-reverse
9-clear
Selected option is : '''))

if select == 1:
    n = int(input("The item which you have to add at the end of your list: "))
    list.append(n)
    print("The appended list is",list)

elif select == 2:
    n = int(input("The item which you want to add : "))
    r= int(input("At which position you have to add the element from 0 to {}".format(l)))
    list.insert(r,n)
    print("The new list is:",list)

elif select == 3:
    n = int(input("'remove' method remove's the first item from the list whose value is equal to the input that you'll give\n The item which you have to remove from the list:  "))
    list.remove(n)
    print("The new list is:",list)

elif select == 4:
    i = int(input("Mention the position of the item from 0 to {} you want to remove: ".format(l - 1)))
    list.pop(i)
    print("The new list is",list)

elif select == 5:
    n = int(input("The element whose lowest index will be returned : "))
    start = int(input("The position from where the search begins from 0 to {} :".format(l - 1)))
    end = int(input("The position from where the search ends from 0 to {} :".format(l - 1)))
    print("The index is {} ".format(list.index(n,start,end)))

elif select == 6:
    n = int(input("The element whose count you want to know :"))
    print("The count of the element {} is {} ".format(n,list.count(n)))

elif select == 7 :
    list.sort()
    print("The list is now sorted:", list)

elif select ==8:
    list.reverse()
    print("The reversed list is:",list)

elif select == 9:
    list.clear()
    print("The cleared list is :",list)

else:
    print("The selected option is not present.Do try the other option's!!!")

print("You can implement different method's too :)")
