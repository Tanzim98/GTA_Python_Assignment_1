# Python Program to Sort a Dictionary by Keys

my_dict = {"b": 2, "a": 1, "d": 4, "c": 3}

sorted_dict = dict(sorted(my_dict.items()))

print("Original Dictionary:", my_dict)
print("Sorted by Keys:", sorted_dict)