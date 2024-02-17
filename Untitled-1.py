i=0
while i<3:
    username=input("input username:")
    password=input("unput password:")
    if username=="admin"and password=="88":
        print('login succeed')
        i=8
    else:
        if i<2:
            print("incorrect",2-i,"chance")
        i+=1
else:
    print('no chance')