# Tuple is an ordered collection of items enclosed in parentheses.

fruit_tuple = ("apple", "banana", "orange", "grapes")
print(fruit_tuple)

number_tuple = (1, 2, 3, 4, 5)
print(number_tuple)

# A tuple can contain different data types.
mixed_tuple = ("apple", 100, 3.14, True, None)
print(type(mixed_tuple))
print(mixed_tuple)

# Indexing
print(mixed_tuple[0])
print(mixed_tuple[-1])

# Slicing: the ending index is not included.
my_tuple = (20, 30, 40, 50)
print(my_tuple[0:3])

# A tuple is immutable, so its items cannot be changed.
print(my_tuple)

# A one-item tuple needs a trailing comma.
single_item_tuple = (10,)
print(single_item_tuple)
print(type(single_item_tuple))

# Concatenation
tuple1 = (89, 90, 56)
tuple2 = (45, 89, 56)
print(tuple1 + tuple2)

# Common tuple functions
values = (78, 89, 45, 12, 48)
print(min(values))
print(max(values))
print(len(values))
print(sorted(values))