first = int(input("First number "))
second = int(input("Second number "))
third = int(input("Third number "))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)