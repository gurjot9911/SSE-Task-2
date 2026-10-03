a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a >= c):
    print("1st num is the greatest")
elif (b >= a and b >= c):
    print("2nd num is the greatest")
else:
    print("3rd num is the greatest")
