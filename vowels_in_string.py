name = input("Enter a string:")
count = 0
for char in name:
    if char in "aeiouAEIOU":
        count += 1
print(count)