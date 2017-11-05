print("Hello my name is Hieu, here is my flock")
sheep = [2, 5, 300, 90, 24, 50, 75]
print(sheep)
p = int(input("How long do you want to feed them ? "))
for n in range(p):
    print("MONTH", n + 1)
    print("One month has passed, now here is my flock ")
    for m in range(len(sheep)):
        sheep[m] = sheep[m] + 50
    print(sheep)
    print("After one month my biggest sheep is has size", max(sheep), 'let`s shear it')
    for i, j in enumerate(sheep):
        if j == max(sheep):
            sheep[i] = 8
            print(sheep)
            print('*'*40)
            break
sum_sheep = sum(sheep)
print("My flock has size in total :", sum_sheep)
print("I would have", sum_sheep * 2, '$' )
