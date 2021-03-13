a = float(input())
b = float(input())
c = float(input())

if a + b > c:
    if b + c > a:
        if a + c > b: 
            print("Possible")
        else:
            print("Not Possible")   
    else:
        print("Not Possible")    
else:
    print("Not Possible")