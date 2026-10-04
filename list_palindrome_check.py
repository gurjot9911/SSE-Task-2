a = int(input("Enter num_1 here: "))
b = int(input("Enter num_2 here: "))
c = int(input("Enter num_3 here: "))
d = int(input("Enter num_4 here: "))
e = int(input("Enter num_5 here: "))
list_1 = [a,b,c,d,e]
list_2 = list_1.copy()
list_2.reverse()
if (list_2 == list_1):
    print("given list is palindrome")
else:
    print("given list is not palindrome")