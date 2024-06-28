matrix_1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]

print(matrix_1[1][1]) # this goes in second list and second element in the list.

# Print all elements using FOR loop, this goes inside each row = list, and fetch each item from each row. end =" " prints items in horizontal and spaced.
for row in matrix_1:
    for item in row:
        print(item, end=" ")