calls = 0

def count_calls():
    global calls
    calls += 1
    
def string_info(stroka):
    list_ = ()
    temp_list = list(list_)
    temp_list.append(len(stroka))
    temp_list.append(stroka.upper())
    temp_list.append(stroka.lower())
    list_ = tuple(temp_list)
    count_calls()
    return list_
    
def is_contains(stroka, list_to_search):
    str_upper = stroka.upper()
    for i in range(len(list_to_search)):
        if str_upper in list_to_search[i].upper():
            return True
    return False
    
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)