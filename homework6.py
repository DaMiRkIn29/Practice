my_dict = {"Anton": 2000, "Sophie": 1997, "Jeff": 1896, "Jesus": 0}
print("Dict:", my_dict)
print("Existing value:", my_dict.get("Sophie"))
print("Not existing value:", my_dict.get("Senior"))
my_dict.update({"Tom": 2012, "George": 2002})
print("Deleted value:", my_dict.pop("Anton"))
print("Modified dict:", my_dict)
print()
my_set = {1, 1, 1, 2.5, 2.5, "Hello", "Hello", (1,2,3)}
print(my_set)
my_set.add("First element")
my_set.add("Second element")
my_set.discard("Hello")
print(my_set)