x,y = map(int,input("Enter a range like (10-20):").split("-"))
factor = 0
for num in range(x if x!=1 else 2,y+1):
    prime = True
    if num>3 and (num%2==0 or num%3==0):
        prime =False
    else:
        fact = 5
        while fact * fact <= num:
            if num % fact ==0 or num %(fact + 2) == 0:
                prime = False
                break
            fact += 6
    if prime:
        print(num)