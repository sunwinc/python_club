array = [[23,45,43,23,45],
         [45,67,54,32,45],
         [89,90,87,65,44],
         [23,45,67,32,10]]

print(array)
print(array[0])
print(array[2])
print(array[0][2])
print(array[2][3])

for rows in array:
    for columns in rows:
        print(columns, end=" ")
    print()


#insert the row at 5 th position
array.insert(2, [1,2,3,4,5])

#insert the row at 6 th position
array.insert(2, [1,2,3,4,5])

#insert the row at 7 th position
array.insert(2, [1,2,3,4,5])

#display
print(array)

#creare 2D array with 4 rows and 5 columns
array=[[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]]

#update row values in the 3rd row
array[2]=[0,3,5,6,7]

#update row values in the 5th row
array[2]=[0,3,5,6,7]

#update the first row , third column
array[0][2]=100

#update the second row , third column
array[1][2]=400

#display
print(array)