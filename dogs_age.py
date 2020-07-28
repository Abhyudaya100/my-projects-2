'''
.Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

Input a dog's age in human years: 15 The dog's age in dog's years is 73

Input: 12
Output: 61
'''
x = int(input("Enter dog's age in human years :"))
if x<=2:
    y = x*10.5
else:
    y = 10.5*2 + 4*(x-2)
print("dog's age in dog's years :",y)