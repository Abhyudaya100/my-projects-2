x,y =(input("Enter a range to find prime numbers:")).split(" ")
x,y = int(x), int(y)
factor = 0
for num in range(x,y+1):
    for i in range(2,num):
        if num%i ==0:
            break
        else:
            print(num)
            break