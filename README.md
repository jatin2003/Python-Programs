## LIST OF PROGRAMS FOR CLASS XII PRACTICAL RECORD

### 1. Write a menu driven program to display fibonacci series or print factorial of a given number.

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

### 2. Write a menu driven program to check whether a string is palindrome or not and check whether one number is prime or not.

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

### 3. Write a program to accept a set of integers and find whether those numbers are palindromes or not.

```py
while True:
    no=int(input("Enter a number:"))
    temp=no
    rev=0
    while no>0:
        rem=no%10
        rev=(rev*10)+rem
        no=no//10
    if temp==rev:
        print(temp,"is palindrome")
    else:
        print(temp,"is not palindrome")
    ch=input("Do you want to continue(y/n):")
    if ch in 'nN':
        break
```

### 4. Write a python program for binary search using a function.

```py
def bsearch(ar,n,item):
    beg=0
    last=len(ar)-1
    while(beg<=last):
        mid=(beg+last)//2
        if(item==ar[mid]):
            return mid
        elif (item>ar[mid]):
            beg=mid+1
        else:
            last=mid-1
    else:
        return -1
n=int(input('Enter size of list:'))
print('Enter numbers in sorted order:\n')
ar=[0]*n
for i in range(n):
    ar[i]=int(input('Element '+str(i)+':'))
item=int(input('Enter the number to be searched:'))
index=bsearch(ar,n,item)
if index>-1:
    print('\nElement found at index:',index,', position:',(index+1))
else:
    print('\nSorry, The given number is not found')
```

### 5. Write a python program by using a function to do bubble sort.

```py
def bubblesort(a, number):
    for i in range(number -1):
        for j in range(number - i - 1):
            if(a[j] > a[j + 1]):
                temp = a[j] # a[j],a[j+1]=a[j+1],a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
a = []
number = int(input("Enter the total number of Elements : "))
for i in range(number):
    value = int(input("Enter the %d Element of List : " %i))
    a.append(value)
bubblesort(a, number)
print("The Sorted List in Ascending Order : ", a)
```

### 6. Write a python program by using a function to do linear search.

```py
def lsearch(ar,n,item):
    for i in range(0,n):
        if ar[i]==item:
            return i
            break
    return -1
n=int(input('Enter size of list:'))
print('Enter numbers in sorted order:\n')
ar=[0]*n
for i in range(n):
    ar[i]=int(input('Element '+str(i)+':'))
item=int(input('Enter number to search:'))
index=lsearch(ar,n,item)
if index!=-1:
    print('\nElement found at index :',index,',position: ',(index+1))
else:
    print('\Sorry, the given number is not found')
```

### 7. Write a program by using a function to find the sum of the following series: x – x2 /2! + x3/3! – …….. – x6/6!

```py
def sumseries(x):
    fact = 1
    sum = 0
    for i in range(1,7):
        fact = fact * i
        if i % 2 == 0 :
            sum = sum - (x**i)/fact
        else :
            sum = sum + (x**i)/fact
    print("Sum of the given series: ",sum)
x = int(input("Enter a term: "))
sumseries(x)
```

### 8. Write a program to have following functions: 

(i) A function that takes a number as argument and calculates cube for it. The function does not return a value .If there is no value passed to the function in function call, the function should calculate cube of 2.

```py
def cube( a = 2 ) :
    print( "Cube of ", a ,":" , a ** 3 )
num = input("Enter a number: ") # For empty press Enter
if num == "" :
    cube()
else :
    cube(int(num))
```

(ii) A function that takes two char arguments and returns True if both the arguments are equal otherwise False. Test both these functions by giving appropriate function call statements.

```py
def chr(char1, char2):
    if char1 == char2:
        return True
    else:
        return False
char1 = input("Enter a Char 1: ")
char2 = input("Enter a Char 2: ")
result=chr(char1,char2)
if result==True:
    print("Both the characters are equal")
else:
    print("Both the characters are unequal")
```

### 9. Write a function that takes two numbers and returns the number that has minimum one's digit.
[For example, If numbers passed are 491 and 278, then the function will return 491 because it has got minimum one's digit out of two given numbers (491's 1 is < 278's 8)].

```py
def min(x , y ) :
    a = x % 10
    b = y % 10
    if a < b :
        return x
    else :
        return y
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Minimum one's digit number: " , min( first , second ) )
```

### 10. Write a program that generates a series using a function which takes first and last values of the series and then generates four terms that are equidistant.
[For example, If two numbers passed are 1 and 7 then function returns 1 3 5 7.]

```py
def ser( a , b ) :
    d = int ( ( b - a ) / 3 )
    print("Series: " , a , a + d , a + 2*d , b )
first = int(input("Enter first Term: "))
last = int(input("Enter last Term: "))
ser(first , last )
```

### 11. Write a program to read the contents of file and display the total number of uppercase ,digit, lower case and special characters.

```py
file=open("story.txt","r")
u=l=spl=d=0
for line in file:
    for word in line:
        for ch in word:
            if ch.isupper():
                u+=1
            elif ch.islower():
                l+=1
            elif ch.isdigit():
                d+=1
            else:
                spl+=1
print("Total number of uppercase characters:",u)
print("Total number of lowercase characters:",l)
print("Total number of digit characters:",d)
print("Total number of special characters:",spl)
```

### 12. Write a function `countmy()` in python to read the text file "Data.txt" and count the number of times "my" occurs in the file.

```py
def countmy(file):
    c=0
    for line in file:
        line=line.split()
        for word in line:
            word=word.lower()
            if word=='my':
                c+=1
    return c

file=open('data.txt','r')
totw=countmy(file)
print("My occurs ",totw,"times.")
```

### 13. Write a program to read a file "Top.txt" and print the contents of file along with the number of lines started with ‘A’.

```py
def linesA(file):
    c=0
    lines=file.readlines()
    for line in lines:
        if line[0]=='A' or line[0]=='a':
            c+=1
    return c

file=open("story.txt","r")
tot=linesA(file)
print("Total number of lines starting with A:",tot)
```

### 14. Write a function Div3and5() that takes a 10 elements numeric tuple and return the sum of elements which are divisible by 3 and 5.

```py
def Div3and5(ar):
    sum=0
    for element in ar:
        if element%3==0 or element%5==0:
            sum+=element
    return sum

t=eval(input("Enter 10 integer values : "))
tot=Div3and5(t)
print("Total Sum :",tot)
```

### 15. Write a program to create binary file to store RollNo, Name and Marks and update marks of entered RollNo.

```py
import pickle
student=[]
file=open("student.dat","wb")
while 1:
    roll=int(input("Enter Roll number:"))
    name=input("Enter Name:")
    marks=int(input("Enter marks:"))
    student.append([roll,name,marks])
    print("Data saved sucessfully..")
    ch=input("Do you want to continue(y/n):")
    if ch in 'Nn':
        break
    pickle.dump(student,file)
file.close()
file=open("student.dat","rb+")
student=[]
data=pickle.load(file)
file.seek(0)
rno=int(input("Enter the roll number to be update:"))
flag=0
rec=[]
for i in data:
    if i[0]==rno:
        print("Name:",i[1])
        print("Current Marks:",i[2])
        i[2]=int(input("Enter new marks: "))
        print("Record updated sucessfully...")
        flag=1
        rec.append(i)
    else:
        rec.append(i)
pickle.dump(rec,file)
if flag==0:
    print("Given roll number not found...")
file.close()
print("Updated data details:")
file=open('student.dat',"rb")
student=[]
student=pickle.load(file)
print(student)
file.close()
```

### 16. Program to create binary file to store rollno and name and search any rollno and display name if rollno found otherwise "Roll no not found".

```py
import pickle
file=open("student.dat","wb")
while 1:
    roll=int(input("Enter Roll Number:"))
    name=input("Enter Name:")
    data=[roll,name]
    pickle.dump(data,file)
    print("Data saved Sucessfully..")
    ch=input("Do you want to enter more data(y/n):")
    if ch in 'nN':
        break
file.close()
file=open("student.dat","rb")
rno=int(input("Enter the roll number to be search:"))
flag=0
try:
    while 1:
        data=pickle.load(file)
        if data[0]==rno:
            print(data[1])
            flag=1
            break
except EOFError:
    print("No more data")
if flag==0:
    print("Roll number not found..")
file.close()
```

### 17. Write a Python program to write a nested Python list( contains Item_Name, description and price) to a CSV file in one go. After writing the CSV file read the CSV file and display the content.

```py
import csv
fh=open("items.csv","w",newline='')
iwriter=csv.writer(fh)
ans="y"
itemrec=[["Item_Name","Description","Price"]]
print("Enter Item Details")
while ans=="y" or ans=="Y":
    iname=input("Enter Item Code : ")
    desc=input("Enter description : ")
    price=float(input("Enter price : "))
    itemrec.append([iname,desc,price])
    ans=input("Do you want to enter more Items(Y/N):")
else:
    iwriter.writerows(itemrec)
    print("Records written successfully")
fh.close()

file=open("items.csv","r")
ireader=csv.reader(file)
for i in ireader:
    print(i)
file.close()
```

### 18. Write a python program to implement a stack using a list data-structure.

```py
s=[]
def push():
    global s
    if len(s)>=5:
        print("Stack Over Flow")
    else:
        roll=int(input("Enter roll:"))
        name=input("Enter name:")
        marks=int(input("Enter marks:"))
        s.append([roll,name,marks])
        print("Sucessfully added your details")
def pop():
    global s
    if len(s)==0:
        print("Stack Under flow")
    else:
        print(s[-1],"popped now")
        s.pop(-1)
def display():
    global s
    if len(s)==0:
        print("Stack is empty now")
    else:
        for i in range(len(s)-1,-1,-1):
            print(s[i])
while 1:
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")
    ch=int(input("Enter you choice:"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Invalid choice")
```

### 19. Write a python program to implement a queue using a list data structure.

```py
q=[]
def enqueue():
    global q
    if len(q)>=5:
        print("Queue is full")
    else:
        roll=int(input("Enter roll:"))
        name=input("Enter name:")
        marks=int(input("Enter marks:"))
        data=[roll,name,marks]
        q.append(data)
        print("Your data saved sucessfully")
def dequeue():
    global q
    if len(q)==0:
        print("Queue is empty")
    else:
        print(q[0]," deleted")
        q.pop(0)
def display():
    global q
    if len(q)==0:
        print("Queue is empty now")
    else:
        print(q)
while 1:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Invalid choice")
```

### 20. Write a program to connect with database and store record of employee and display record.

```py
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='')
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS COMPANY")
cur.execute("USE COMPANY")
cur.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE(EMPNO INT,NAME CHAR(35),DEPT CHAR(35),SALARY INT)")
con.commit()
while 1:
    print("1.ADD")
    print("2.DISPLAY")
    print("3.EXIT")
    ch=int(input("Enter Choice:"))
    if ch==1:
        e=int(input("Enter employee no"))
        n=input("Enter name:")
        d=input("Enter department:")
        s=int(input("Enter salary:"))
        q="insert into employee values({},'{}','{}',{})".format(e,n,d,s)
        cur.execute(q)
        con.commit()
        print("Data Saved sucessfully")
    elif ch==2:
        q="select * from employee"
        cur.execute(q)
        result=cur.fetchall()
        for row in result:
            print(row)
    elif ch==3:
        break
    else:
        print("Invalid choice")
```

### 21. Write a program to connect with database and search employee numbers in table and display record, if employee number not found display appropriate message.

```py
import mysql.connector as mysql
con=mysql.connect(host='localhost',user='root',password='')
cur=con.cursor()
cur.execute("DROP DATABASE COMPANY")
cur.execute("CREATE DATABASE COMPANY")
cur.execute("USE COMPANY")
cur.execute("CREATE TABLE EMPLOYEE(EMPNO INT,NAME CHAR(35),DEPT CHAR(35),SALARY INT)")
con.commit()
while 1:
    print("1.Add")
    print("2.Search")
    print("3.Exit")
    ch=int(input("Enter Choice:"))
    if ch==1:
        e=int(input("Enter Employee no: "))
        n=input("Enter name: ")
        d=input("Enter department: ")
        s=int(input("Enter salary: "))
        q="insert into employee values({},'{}','{}',{})".format(e,n,d,s)
        cur.execute(q)
        con.commit()
        print("Data saved successfully")
    elif ch==2:
        q="select * from employee"
        cur.execute(q)
        s=int(input("Enter the roll number to be search: "))
        result=cur.fetchall()
        for row in result:
            if row[0]==s:
                print(row)
                break
            else:
                print("Given roll number not found")
    elif ch==3:
        break
    else:
        print("Invalid choice")
```

### 22. Write a program to connect with database and update the employee record by entered employee number.

```py
import mysql.connector as mysql
con=mysql.connect(host='localhost',user='root',password='')
cur=con.cursor()
cur.execute("DROP DATABASE COMPANY")
cur.execute("CREATE DATABASE COMPANY")
cur.execute("USE COMPANY")
cur.execute("CREATE TABLE EMPLOYEE(EMPNO INT,NAME CHAR(35),DEPT CHAR(35),SALARY INT)")
con.commit()
while 1:
    print("1.ADD")
    print("2.UPDATE")
    print("3.DISPLAY")
    print("4.EXIT")
    ch=int(input("Enter Choice:"))
    if ch==1:
        e=int(input("Enter employee no:"))
        n=input("Enter name:")
        d=input("Enter department:")
        s=int(input("Enter salary:"))
        q="insert into employee values({},'{}','{}',{})".format(e,n,d,s)
        cur.execute(q)
        con.commit()
        print("Data saved sucessfully")
    elif ch==2:
        no=int(input("Enter the emp no to be update:"))
        cur.execute("select * from employee where empno={}".format(no))
        data=cur.fetchall()
        if cur.rowcount==0:
            print("Given data not found")
        else:
            print("You can update only department and salary of employee")
            dep=input("Enter new department:")
            sal=int(input("Enter new salary:"))
            try:
                q="update employee set dept='{}' ,salary={} where empno={}".format(dep,sal,no)
                cur.execute(q)
                con.commit()
                print("Update sucessfully")
            except Exception as e:
                print(e,"found")
    elif ch==3:
        cur.execute("select * from employee")
        data=cur.fetchall()
        print(data)
    elif ch==4:
        break
    else:
        print("Invalid choice")
```

### 23. Write a program to connect with database and delete the record of entered employee number.

```py
import mysql.connector as mysql
con=mysql.connect(host='localhost',user='root',password='')
cur=con.cursor()
cur.execute("DROP DATABASE COMPANY")
cur.execute("CREATE DATABASE COMPANY")
cur.execute("USE COMPANY")
cur.execute("CREATE TABLE EMPLOYEE(EMPNO INT,NAME CHAR(35),DEPT CHAR(35),SALARY INT)")
con.commit()
while 1:
    print("1.ADD")
    print("2.DELETE")
    print("3.DISPLAY")
    print("4.EXIT")
    ch=int(input("Enter Choice:"))
    if ch==1:
        e=int(input("Enter employee no:"))
        n=input("Enter name:")
        d=input("Enter department:")
        s=int(input("Enter salary:"))
        q="insert into employee values({},'{}','{}',{})".format(e,n,d,s)
        cur.execute(q)
        con.commit()
        print("Data Saved sucessfully...")
    elif ch==2:
        no=int(input("Enter the emp no to be deleted:"))
        cur.execute("select * from employee where empno={}".format(no))
        data=cur.fetchall()
        if cur.rowcount==0:
            print("Given data not found")
        else:
            q="delete from employee where empno={}".format(no)
            cur.execute(q)
            con.commit()
            print("Deleted sucessfully")
    elif ch==3:
        cur.execute("select * from employee")
        data=cur.fetchall()
        print(data)
    elif ch==4:
        break
    else:
        print("Invalid choice")
```