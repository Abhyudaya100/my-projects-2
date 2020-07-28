N,k = input().split(",")
N,k = int(N),int(k)
factors = []
if 1<N<10000000000 and 1<k<600:
    for x in range(1,N+1):
        if N % x == 0:
            factors.append(x)
        x += 1
if k<=len(factors):
    print(factors[k])
else:
    print('1')