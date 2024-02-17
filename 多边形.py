for i in range(1,4):
    for j in range(1,5):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(1,7-i):
       print("x",end="")
    print()

for j in range(1,6-i):
    print(" ",end="")
for k in range(i,i*2):
    print("*",end="")