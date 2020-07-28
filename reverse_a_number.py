n = int(input("Enter a number :"))

while n!= 0:
    remainder = n%10
    print(remainder, end="")
    n//=10