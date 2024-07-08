immutable_var = 1, 2, True, "Привет"
print("Immutable tuple:", immutable_var)
# "immutable_var[0] = False" выдаст ошибку, т.к. в кортеже, в отличие от массивов, все аргументы являются константой и их изменить нельзя
mutable_list = [False, True, "Снова привет", 1, 15]
mutable_list[1] = "Изменил"
mutable_list[2] = "Массив"
print("Mutable list:", mutable_list)