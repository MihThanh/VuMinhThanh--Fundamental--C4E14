n = int(input("Enter a number: "))
#print(*range(n)) #Không cần hàm for tự in trên 1 dòng
# for i in range(n):
#     print (i, end = ' ')

# for i in range(0,n,2):
#     print(i, end = ' ')
#print()
for i in range(n):
    if(i%2 == 0):
        print("Fizz")
    elif(i%3 == 0):
        print("Buzz")
    elif(i%2 == 0 and i%3 == 0):
        print("Fizz Buzz")
print()
