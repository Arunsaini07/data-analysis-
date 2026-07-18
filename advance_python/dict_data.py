#------- these are all the comphehension examples in python --------



# names = ["Alice", " BOB ", " Charlie ", " David ", "EVE"]
# prices = [10.5, 20.0, 15.75, 30.0, 25.5]

# # product_dict = {name: price for name, price in zip(names, prices)}
# # another way to write the same function
# product_dict = {names[i]: prices[i] for i in range(len(names))}

# print(product_dict)

# score = {'Alice': 10.5, ' BOB ': 20.0, ' Charlie ': 15.75, ' David ': 30.0, 'EVE': 25.5}

# passed = {K: V for K, V in score.items() if V >= 20.0}

# print(passed)

# values = [23, 45,45,45, 12, 67, 34, 89, 56]

# unique_squares = {x**2 for x in values}
# print(unique_squares)


nested_comprehension = [[(i , j) for j in range(1, 6)] for i in range(1, 6)]
# same thing with help of for loop 

for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append((i , j))
    print(row)
print(nested_comprehension)