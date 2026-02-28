#task's
# 1.patterns-01 matrix
n=3
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=" ")
    print()

#2.alphabet pattern
n=3
for i in range(n):
    for j in range(n):
            print(chr(65+i)*n)
    print()

#3.star square
a=4
for i in range(a):
    for j in range(a):
        if i==0 or i==a-1 or j==0 or j==a-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
#7.number pattern       
a=4
for i in range(a):
    for j in range(a):
        if i==0 or i==a-1 or j==0 or j==a-1:
            print("1",end=" ")
        else:
            print(" ", end=" ")
    print()
#4.star box
a=4
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or j == 0 or j ==a-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

#5.single line pattern
a=4
for i in range(a):
    for j in range(a):
        if i==j:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()


#6.x pattern
a=5
for i in range(a):
    for j in range(a):
        if i==j or i+j==a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


























