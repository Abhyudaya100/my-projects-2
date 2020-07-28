N = int(input())
bridestobe,groomstobe = (input().split(" "))
bridestobe = list(bridestobe)
groomstobe = list(groomstobe)
if (len(bridestobe) and len(groomstobe)) == N:
    for i in bridestobe:
        if (i in groomstobe):
            groomstobe.remove(i)
        else:
            break
print(len(groomstobe))