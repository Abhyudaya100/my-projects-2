n =int(input())
primenos = []
for num in range(2,n+1):
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
count=0
for index in range(2,len(primenos)):
    primesum = sum(primenos[:index])
    if primesum<=n and primesum in primenos:
        count+=1
print(count)
