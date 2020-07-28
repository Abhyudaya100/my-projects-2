import  math
num = int(input())

if num == 1:
    print("neither prime nor composite")
else:
    for fact in range(2,int(math.sqrt(num))+1):
        if num %fact ==0:
            print("not prime")
            break;
    else:
        print("prime")