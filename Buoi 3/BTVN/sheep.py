sheep_size = [5, 7, 300, 90, 24, 50, 120 ]
print("Hello my name is Thanh and there are my sheep size: ")
print(sheep_size)
print("Now my biggest sheep has size {0} let 's shear it".format(max(sheep_size)))
for index, item in enumerate(sheep_size):
    if item == max(sheep_size):
        sheep_size[index] = 8
        break
print("After shearing, here is my flock")
print(sheep_size)

print("One month has passed, now here is my flock")
for i in range(len(sheep_size)):
    sheep_size[i] += 50
print(sheep_size)
