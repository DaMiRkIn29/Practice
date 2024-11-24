"""def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)""" #При сложении дает вывод 130.45600000000002, поэтому код ниже округляет результат

def add_everything_up(a, b):
    try:
        result = a + b
        return round(result, 3)
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))