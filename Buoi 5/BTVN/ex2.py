n = int(input("Enter a number: "))
count = 0
for i in range(2, n):
    if n % i == 0:
        count += 1
if count != 0:
    print("{0} is not a prime number".format(n))
else:
    print("{0} is a prime number".format(n))
