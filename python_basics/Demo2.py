# basics of Python2
values = [1, 2, 'nate', 4, 5]
# list allows multiple values and datatypes

print(values[0])
# >1

print(values[-1])
# shortcut to print last value in list

print(values[1:3])
# >[2, nate] (exclusive to the last index)

values.insert(3, 'taylor')
print(values)
# [1, 2, 'nate', 'taylor', 4, 5]

values.append('end')
# add value to the end of the list

values[2] = 'NATE'
# updates value at index 2

del values[0]
# delete value at index 0

print(values)
# >[2, 'NATE', 'taylor', 4, 5, 'end']
