from util_fonctions import is_sorted, valid_differences, is_safe

# Tests de is_sorted
assert is_sorted([1, 2, 3, 4]) == True
assert is_sorted([4, 3, 2, 1]) == True
assert is_sorted([1, 3, 2, 4]) == False
assert is_sorted([2, 2, 3]) == False

# Tests de valid_differences
assert valid_differences([1, 2, 3]) == True
assert valid_differences([4, 6, 9]) == True
assert valid_differences([1, 5]) == False
assert valid_differences([10, 10]) == False

# Tests de is_safe
assert is_safe([1, 3, 4]) == True
assert is_safe([5, 3, 2]) == True
assert is_safe([1, 2, 2]) == False
assert is_safe([1, 5, 6]) == False
assert is_safe([3, 1, 2]) == False

print("Tous les tests sont passés avec succès.")
