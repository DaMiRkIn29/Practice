def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25) 
print_params(c = [1,2,3])

values_list = [1, "Stroka", False]
values_dict = {"a": 1, "b": 'строка', "c": True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

all_values = [1, "Stroka", False, 54.32]

for i in all_values:
    print(i)