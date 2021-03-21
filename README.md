# LIST OF PROGRAMS FOR CLASS XII PRACTICAL RECORD

1. Write a menu driven program to display fibonacci series or print factorial of a given number.

```py
while 1:
    print("1. Fibonacci Series")
    print("2. Factorial")
    print("3. Exit")
    opt=int(input("Enter your choice:"))
    if opt==1:
        n=int(input("Enter no. of terms:"))
        no1=0
        no2=1
        print("The first",n,"terms of fibonacci series:")
        print(no1)
        print(no2)
        for i in range(n-2):
            no3=no1+no2
            print(no3)
            no1=no2
            no2=no3
    elif opt==2:
        f=1
        no=int(input("Enter no:"))
        for i in range(1,no+1):
            f=f*i
            print("Factorial is:",f)
    elif opt==3:
        break
    else:
        print("Invalid Choice!")
```

2. Write a menu driven program to check whether a string is palindrome or not and check whether one number is prime or not.

```py
while 1:
    print("1. Palindrome")
    print("2. Prime Number")
    print("3. Exit")
    opt=int(input("Enter your choice:"))
    if opt==1:
       name=input("Enter text:")
       rev=name[::-1]
       if name==rev:
           print(name,"is palindrome")
       else:
           print(name,"is not palindrome")
    elif opt==2:
        no=int(input("Enter number:"))
        for i in range(2,no):
            if no%i==0:
                print("The given no is not a prime number")
                break
        else:
             print("The given number is a prime number")   
    elif opt==3:
        break
    else:
        print("Invalid Choice!")
```
