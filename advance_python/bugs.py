# a = [3,4,44,55,66,77,88,99]

# b=a
# b[1]=100
# b[2]=200
# b[3]=300
# b[4]=400
# b[5]=500
# b[6]=600
# b[7]=700
# print(a)
# print(b)


def add_items(item):
    item.append(10)

data = [1, 2, 3, 4, 5]
add_items(data.copy())  # Pass a copy of the list to avoid modifying the original
print(data)  # Output: [1, 2, 3, 4,
