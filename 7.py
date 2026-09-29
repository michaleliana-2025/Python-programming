#else if statements behaves for mutually exclusive event
mark= 75
if mark >= 70:
    print ("Grade B")
    if mark >=80:
        print ("Grade A")
    if mark >=90:
        print ("Grade O")
    else: 
        print ("Fail")
        
    