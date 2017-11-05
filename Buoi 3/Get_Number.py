from random import randint
n= randint(1,100)
print(n )
kq = True
while kq:
    a= int(input("Nhap 1 so: "))
    if a==n:
        print("Chinh xac")
        #kq= False
        break
    elif a < n:
        print("Tang len di")
    else:
        print("Giam xuong di")
