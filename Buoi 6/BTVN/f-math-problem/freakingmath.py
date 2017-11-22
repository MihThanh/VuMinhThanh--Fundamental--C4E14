from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
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
    if user_choice:
        if generate_quiz() != result:
            return True
        else:
            return False
    else:
        if generate_quiz() == result:
            return False
        else:
            return True
