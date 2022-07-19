#Python Lambda Functions are anonymous function means that the function is without a name. 
# As we already know that the def keyword is used to define a normal function in Python. 
# Similarly, the lambda keyword is used to define an anonymous function in Python. 

#syntax : lambda arguments: expression

#function
def add(x,y):
    return x+y

#lambda
lambda x,y: x+y

#map function - applies the given function to each item of a given iterable (list, tuple etc.)
#syntax: map(function,sequence)

#find the square of each element os the list

def sqaure(n):
    return n**2

list1= [1,2,3,4]
print(map(sqaure,list1)) #returns the address of where list is stored in the memory

#to find the output-
#print(list(map(sqaure,list1)))

#using lamda function
print(list(map(lambda x: x**2,list1)))
