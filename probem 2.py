'''
Problem 2:
FACTORS OF X

One day a teacher gave an assignment to the student to find the factors of a number. The student is not interested to do the given task and he was searching for the shortcuts. So, please help him by writing a program
Input Format
First line contains an integer T denoting the no.of testcases.
The next T lines contains integers whose factors we have to determine
Constraints
1<=T<=10000
1<=N<=1000000
Output Format
Factors of number separated by a space in the new line
Sample Input 0
2
4
5
Sample Output 0
1 2 4
1 5
'''
T = int(input("Enter the number of testcases :"))
N = [int(input("Enter the numbers whose factor to be found:")) for _ in range(T)]
if 1<=T<=10000:
    for n in N:
        if 1<=n<=1000000:
            for factor in range(1, n + 1):
                if n % factor == 0:
                    print(factor, end=" ")
                factor += 1
            print(end="\n")
        else:
            exit(0)
else:
    exit(0)