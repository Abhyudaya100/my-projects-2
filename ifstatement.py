P = int(input("Principle : "))
R = float(input("Rate : "))
T = float(input("Time : "))

print("Enter '1' for Simple Interest")
print("Enter '2' for Compound Interest")
choice = int(input("Enter your choice :"))
if choice == 1:
    interest = (P*T*R)/100
else :
    interest = P*(1+R/100)**T-P

print("Interest : %f" ,round(interest,2))