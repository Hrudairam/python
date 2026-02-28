n=int(input("enter a number of students:"))
present=0
absent=0
for i in range(1,n+1):
    status=input(f"enter students prsent or absent:")
    if status=="p":
        present +=1
    elif status=="a":
        absent +=1
print("\ntotal students:",n)
print("present:",present)
print("absent:",absent)

'''a=(input("enter the student name:"))
b=(input("enter the college name:"))
c=(input("enter the batch name:"))
d=int(input("enter the fee:"))
e=int(input("enter the hostel fee:"))
print("student name:",a)
print("college name:",b)
print("batch name:",c)
print("college fee:",d)
print("hostel fee:",e)
print("total:",d+e)'''
        
