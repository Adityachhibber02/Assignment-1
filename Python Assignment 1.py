#Q.1
a=int(input("Enter the first number="))
b=int(input("Enter the second number="))
c=int(input("Enter the third number="))
avg=(a+b+c)/3
print(avg)

#Q.2
grossincome=int(input("Enter gross income"))
dependent=int(input("number of dependents"))
taxincome=grossincome-1000-(dependent*3000)
tax=0.2*taxincome
print("income tax=",tax)

#Q.3
s=int(input("SID:"))
n=str(input("Name:"))
g=str(input("Gender:"))
cn=str(input("Course Name:"))
c=float(input("CGPA:"))
stud=[s,n,g,cn,c]
print(stud)

#Q.4
s1=float(input("Enter marks of first student="))
s2=float(input("Enter marks of second student="))
s3=float(input("Enter marks of third student="))
s4=float(input("Enter marks of fourth student="))
s5=float(input("Enter marks of fifth student="))
lst=[s1,s2,s3,s4,s5]
lst.sort()
print(lst)

#Q.5
colour=["red","green","white","black","pink","yellow"]
#Part a
colour.pop(3)
print(colour)
#Part b
colour=["red","green","white","black","pink","yellow"]
colour[3:5]=["purple"]
print(colour)
