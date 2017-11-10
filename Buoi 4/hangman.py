word = ['apple', 'teen', 'fruit','bag','techkid']
from random import *
n = choice(word)
while()
print("Từ của bạn: ")
for i in range(len(n)):
    print("_", end = ' ')
print()
l = list(n)
m = input("Đoán chữ: ")
if m in l:
    print("True")
    for index, item in enumerate(n):
        print(index, 'vs', item)
