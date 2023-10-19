tuple = (1, 2, 3, 4, 5)
element = 6
index = 3
tuple = tuple[:index]+(element,) + tuple[index:]
print(tuple)
