# String Slicing
my_sub= "Machine Learning"
print (my_sub[0:7:1])
print (my_sub[6:0:-1])
print (my_sub[0: :1])
print (my_sub[ : : -1])
print (my_sub[6:0:-1])

#Immutability of String
my_str= "Hello" 
#my_str[0]= "c"
#print (my_str)

#Methods of String

print (my_sub.lower())
print (my_sub.upper())
print (my_sub.replace("Machine", "Deep"))
print (my_sub.count("i"))
print (my_sub.find("i"))
print (my_sub.count ("n", 0, 7))
print (my_sub.split("n"))
print (my_sub)