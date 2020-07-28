'''
Write a Python program to convert month name to a number of days.

List of months: January, February, March, April, May, June, July, August , September, October, November, December Input the name of Month: February No. of days: 28/29 days

Input: May

Output: List of months: January, February, March, April, May, June, July, August, September, October, November, December
Input the name of Month: May
No. of days: 31 day

'''
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month = input("Enter the name of the month :")
if month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
    print("No. of days : 31 days")
elif month == 'april' or month == 'june' or month == 'september' or month == 'november':
    print("No. of days : 30 days")
elif month == 'february':
    print("No. of days : 28/29 days")
else:
    print("Incorrect spelling/Invalid month")