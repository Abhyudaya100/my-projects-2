n= int(input("Enter the number of primes to be displayed:"))
primenos = []
for num in range(2,n**7):
    prime = True
    if num>3 and (num%2==0 or num%3 ==0):
        prime = False
    else:
        fact = 5
        while fact * fact <= num:
            if num % fact == 0 or num % (fact + 2) == 0:
                prime =False
                break
            fact += 6
    if prime:
        primenos.append(num)
        n -= 1
    if n!=0:
        continue
    else:
        print(*primenos)
        exit(0)