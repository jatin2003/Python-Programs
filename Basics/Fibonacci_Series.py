# Program to display Fibonacci Series up to nth term

no = int(input("Enter number of terms: "))
a = 0
b = 1
print(a,b,end=" ")
for i in range(2,no):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
