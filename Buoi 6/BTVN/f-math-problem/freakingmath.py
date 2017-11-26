from random import *
from cal import eval
def generate_quiz():
    x = randint(1, 10)
    y = randint(1, 10)
    error = randint(-1, 1)
    op = choice(['+', '-', '*', '/'])
    if op == '/':
        if y == 0:
            print('NaN')
        else:
            result_true = x / y
    if op == '*':
        result_true = x * y
    if op == '+':
        result_true = x + y
    if op == '-':
        result_true = x - y

    result = result_true + error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    true_result = eval(x, y, op)
    if user_choice:
        return true_result == result
    else:
        return true_result != result
