#init matrix
def genMatrix(rows,cols):  
    #use nested list for matrix
    # matrix = [[0 for col in range(cols)] for row in range(rows)]  
    matrix = []
    for i in range(rows):  
        line = []
        for j in range(cols):  
            line.append(0)
        matrix.append(line)
    # matrix = [[0]*cols]*rows
    print(matrix)
    return matrix

#for the snake fill function
def testSnake(num):
    #call genMatrix
    matrix = genMatrix(num, num)
    i = j = 0
    total = matrix[i][j] = 1
    while(total < num * num):
        #to the right
        while(j + 1 < num and matrix[i][j + 1] == 0): 
            total += 1
            j += 1
            matrix[i][j] = total
        #down direction
        while(i + 1 < num and matrix[i + 1][j] == 0):
            total += 1
            i += 1
            matrix[i][j] = total
        #left direction
        while(j > 0 and matrix[i][j - 1] == 0): 
            total += 1
            j -= 1
            matrix[i][j] = total
        #up direction
        while(i + 1 > 0 and matrix[i - 1][j] == 0): 
            total += 1
            i -= 1
            matrix[i][j] = total
    #print
    for i in range(num):  
            for j in range(num):
                print ('%3d ' % matrix[i][j], end='')
            print()

# test function
while True:
    number = int(input("Please Input your number: "))
    if(number <= 0):
        print("Please input positive number: ")
        continue
    else:
        break
    
testSnake(number)


