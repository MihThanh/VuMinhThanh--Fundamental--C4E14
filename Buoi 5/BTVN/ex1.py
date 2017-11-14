numbers = [1, 7, 16, 18, 20, 3, 1, 16, 18, 18, 100, 18]
n = int(input("Nhap phan tu can dem: "))
count = 0
for i in numbers:
    if i == n:
        count += 1
if count == 0:
    print("Không có phần tử {0} trong dãy".format(n))
else:
    print("{0} xuất hiện {1} lần".format(n, count))
