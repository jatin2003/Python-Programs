# Program to read text file

j=open("Demo.txt",'r')
if not j:
    print ("The file you entered doesn't exist!!")
else:
    r = j.read()
    print (r)
