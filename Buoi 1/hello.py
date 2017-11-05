
# yob = int(input("Your year of birth?"))
# age = 2017 - yob
# print("your age= ", age)
#
# if age < 10:
#     print("Baby")
# elif age < 18 :
#     print("Teenager")
# else:
#     print("Adult")
#
# print("Bye Bye")

a = int(input("a= "))
b= int(input("b= "))
c = int(input("c= "))
delta= b * b - 4 * a * c
if a == 0:
    print("Phuong trinh co nghiem: ", -c/b)
if a != 0:
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        print("Phuong trinh co nghiem: ", -b/(2 * a))
    else :
        print("Phuong trinh co 2 nghiem phan biet: ")
        print("x1 = ", (-b + delta**0.5)/(2 * a))
        print("x2 = ", (-b - delta**0.5)/(2 * a))
        #print("x1= {0}, x2= {1}".format(x1,x2))
