
a = float(input())
b = float(input())
c = float(input())

if a + b > c and b + c > 1 and a + c > b:
    print("Possible")
else:
    print("Not Possible")