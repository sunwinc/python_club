def li_search(li, num):
    for i in range(0, len(li)):
        if li[i] == num:
            return i

def bi_search(li, num):
    low = 0
    high = len(li) - 1
    
    while True:
        m = (low + high)//2
        if li[m] > num:
            high = m - 1
        elif li[m] < num:
            low = m + 1
        else:
            return m 


num_list = [2, 3, 4, 6, 7, 9, 10]
num = 6

print(bi_search(num_list, num))
