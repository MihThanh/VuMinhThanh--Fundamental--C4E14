from random import *
from cal import eval
# import cal
x = randint(0, 10)
y = randint(0, 10)
op = choice(['+', '-', '*', '/'])
error = randint(-1, 1)
true_tong = eval(x, y, op)
# true_tong = cal.eval(x, y, op)
tong = true_tong + error

print('{0} {3} {1} = {2}'.format(x, y, tong, op))

# n = input("(Y/N): ").upper()
# # if n in ['n', 'y']:
# if error == 0:
#     if n == 'Y':
#         print('Dung')
#     elif n == 'N':
#         print('Sai')
# else:
#     if n == 'Y':
#         print('Sai')
#     elif n == 'N':
#         print('Dung')
