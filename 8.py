#for loop: for number of iterations

#1
my_sub="python"
for i in my_sub:
    print(i)

#2
for i in range(len(my_sub)):
    print(my_sub[i],"->", i)

#range: syntax:(SP, EP, SS)

#hw: practice for loop using string, range, list, tuple & dictionary

#3

#while loop: until a condition is met
j=0 #intilization
while j<4:
    print(j)
    j+=1

#hw: practice while loop practice

#4
#break
i=0
while i<4:
    i+=1
    if i==2:
        break
        print(i)
    else:
         print(i)


#5
#continue
i=0
while i<4:
    i+=1
    if i==2:
        continue
        print(i)
    else:
         print(i)
         
#6
#pass
i=0
while i<4:
    i+=1
    if i==2:
        pass
        print(i)
    else:
         print(i)

