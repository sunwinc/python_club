def ins_sort1(A):
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j-1] > A[j]:
                A[j], A[j-1] = A[j-1], A[j]
            else:
                break

def ins_sort2(A):
    for i in range(1, len(A)):
        key = A[i]
        for j in range(i, 0, -1):
            if A[j-1] > key:
                A[j]= A[j-1]
            else:
                break
        if A[0] > key:
            A[0] = key
        else:
            A[j] = key  

def ins_sort3(A):
    for i in range(1, len(A)):
        j = i-1
        while A[j] > A[j+1] and j >= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1

def ins_sort4(A):

    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
                
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j = j - 1
            
        # Place key at after the element just smaller than it.
        A[j + 1] = key

