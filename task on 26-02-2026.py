#mulitiplication table
'''a=int(input("Enter a number: "))
for i in range(1,21):
    print(a,"x", i, "=", a*i)'''

#expense tracker
'''a=input("enter user name:")
b=input("enter the category:")
c=input("enter the amount:")
print("user name:",a)
print("category:",b)
print("amount:",c)'''

#caluculator by using functions
'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("enter the number:"))
b=int(input("enter the another number:"))
print("add:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("div:",a/b)'''


#marks analyzer
#your code
S1=int(input("enter the s1"))
S2=int(input("enter the s2"))
S3=int(input("enter the s3"))
S4=int(input("enter the s4"))
marks=[S1,S2,S3,S4]
highest=max(marks)
lowest=min(marks)
total=sum(marks)
average=total/len(marks)
print("highest marks",highest)
print("lowest marks",lowest)
print("total marks",total)
print("average marks",average)

#marks analyzer
mark=[]
count=int(input("enter the total no.of students"))
for i in range(count):
    mark=int(input("enter the marks"))
    marks.append(mark)
print("\n marks entered")
for j in marks:
    print(j)
heighst=max(marks)
lowest=min(marks)
total=sum(marks)
average=total/len(marks)

















