# Write a python program to perform all set operations. 





# Define two sets for demonstration
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Set Operations
print("Set A:", set_a)
print("Set B:", set_b)

# Union
union_set = set_a | set_b
print("Union (A ∪ B):", union_set)

# Intersection
intersection_set = set_a & set_b
print("Intersection (A ∩ B):", intersection_set)

# Difference
difference_set_a_b = set_a - set_b
difference_set_b_a = set_b - set_a
print("Difference (A - B):", difference_set_a_b)
print("Difference (B - A):", difference_set_b_a)

# Symmetric Difference
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference (A Δ B):", symmetric_difference_set)

# Subset and Superset
is_subset = set_a <= set_b
is_superset = set_a >= set_b
print("Is A a subset of B?", is_subset)
print("Is A a superset of B?", is_superset)

# Adding an element to a set
set_a.add(9)
print("Set A after adding 9:", set_a)

# Removing an element from a set
set_b.remove(8)
print("Set B after removing 8:", set_b)

# Clearing a set
set_a.clear()
print("Set A after clearing:", set_a)