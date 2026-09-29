#list is sequence of items, every item separated by comma and enclosed by square bracket.
fruit_list= ["apple", "banana", "orange", "grapes"]
print (fruit_list)
number_list= [1,2,3,4,5,6,7,8,9,10]
print (number_list)

#hetrogenous list
mixed_list =["apple", 100, 3.14, True, False, None]
print (type((mixed_list)))
print (mixed_list)

# indexing-- location of item
#positive indexing
print (mixed_list[0])

#negative indexing
print (mixed_list[-1])

#slicing 
my_list= [20,30,40,50]
print (my_list[0:3:1])
#last indexing is not included(3)

#property of list
#mutability to change the data of data
my_list= ["apple", 100,True, None]
print(my_list)
my_list[1]=90
print(my_list)

#concatenation--addition of the list
list1=[89,90,56]
list2=[45,89,56]
my_list = list1 + list2
print (my_list)

#function of list
my_list= [78,89,45,12,48]
#min
print (min(my_list))
#max
print (max(my_list))
#length of list

print (len(my_list))

#sorted()-- arrange list in increasing or decreasing order
x= [34,12,56,78,12,45]
print (sorted (x))
print (sorted(x, reverse= True))
print (sorted(x, reverse= False))

x=[12,56,5,78,4,90]
print (x)
#here variable is used before method, where as in print variable is used inside print
x.sort()
print(x)

#adding item at the end of list
my_list= [89,45,67]
my_list.append(1000)
print (my_list)

# appending to an empty list
x=[]
x.append(10)
print(x)
x.append(20)
print(x)

#extend()-- one list merge into another list
list1= [89,78,56]
list2= [23,45,67]
print(list1)
list1.extend(list2)
print (list1)

#pop()-- remove the ietm from the list and take index as a argument
x= [23,45,67,89]
x.pop()
print (x)
x.pop(1)
print (x)

#remove ()-- remove the item from the list and take item as a argument
a =[23,45,67]
print(a)
a.remove(67)
print (a)

#tuple, immutable data type
a= 1,2,3 
print(tuple(a))

#set()-- unorder data structure
my_set={45,67,12,43}
print(my_set)

#set not contain duplicate item
my_list= [12, 13, 12, 14, 12]
print(my_list)

a= set(my_list)
print (a)

d={}
print (type(d))

a= set()
print (type(a))

#set is mutable
x= set ()
print (x)
x.add(10)
print(x)


