sheep_size = [5, 7, 300, 90, 24, 50, 120 ]
print("Hello my name is Thanh and there are my sheep size: ")
print(sheep_size)
m = int(input("Enter your month: "))
for i in range(m):
    print("MONTH", i + 1)
    print("One month has passed, now here is my flock ")
    for j in range((len(sheep_size))):
        sheep_size[j] += 50
    print(sheep_size)
    print("Now my biggest sheep has size {0} let 's shear it".format(max(sheep_size)))
    print("After shearing, here is my flock")
    for index, item in enumerate(sheep_size):
        if item == max(sheep_size):
            sheep_size[index] = 8
            print(sheep_size)
            print()
            break
tong= sum(sheep_size)
print("My flock has size in total: ",tong)
print("I would get {0} * 2$ = {1}".format(tong, tong * 2))
