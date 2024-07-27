data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure):
    count = 0
    if isinstance(structure, (list, tuple, set)):
        for element in structure:
            count += calculate_structure_sum(element)
    elif isinstance(structure, dict):
        for key, value in structure.items():
            count += calculate_structure_sum(key)
            count += calculate_structure_sum(value)
    elif isinstance(structure, str):
        count += len(structure)
    elif isinstance(structure, int):
        count += structure
    return count

result = calculate_structure_sum(data_structure)
print(result)