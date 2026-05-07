#  Python Program to Sort a Dictionary by Values

my_dict = {"a": 3, "b": 1, "c": 4, "d": 2}

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Original Dictionary:", my_dict)
print("Sorted by Values:", sorted_dict)