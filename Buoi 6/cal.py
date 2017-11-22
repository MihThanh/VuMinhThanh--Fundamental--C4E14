def eval(x, y, op):
    if op == '/':
        result = x / y
    elif op == '-':
        result = x - y
    elif op == '+':
        result = x + y
    elif op == '*':
        if y == 0:
            print = 'NaN'
        else:
            result = x * y
    return result
# x = 10
# y = 5
# op = '/'
# r = eval(x, y ,op)
# print(r)

# x = int(input('x = '))
# y = int(input('y = '))
# n = input("phep toan: ")
#
# s = eval()
#
# if op in ['+', '-', '/', '*']:
#     r = eval()
#     print(r)

# Làm phép tính: 5+6= 11 in trên 1 dòng
