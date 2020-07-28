string = input()
no_r = int(input())
firstcharstring = ""

while no_r>0:
    direction, rotation = input().split(" ")
    rotation = int(rotation)
    if direction in ['l','L']:
        firstcharstring += (string[rotation:] + string[:rotation])[0]
    else:
        firstcharstring += (string[-rotation:] + string[:-rotation])[0]
    no_r-=1
print(firstcharstring)

#forming a substring from the original string
"""substrs = []
for row in range(len(string)):
    for col in range(row + 1,len(string) +1):
        if len(string[row:col]) == len(firstcharstring):
            substrs.append(string[row:col])
"""
substrs = [string[row:col] for row in range(len(string)) for col in range(row + 1,len(string) +1) if len(string[row:col]) == len(firstcharstring)]
for substr in substrs:
    if sorted(substr) == sorted(firstcharstring):
        print("YES")
        break
else:
    print("NO")