# def is_daffodil_num(num):
#     # Calculate the sum of each digit raised to the power of the number of digits in the input number.
#     # Check if the result is equal to the original number.
#     i = num // 100
#     j = num // 10 % 10
#     k = num % 10
#     return num == i**3 + j**3 + k**3

def is_daffodil_num(num):
    # Calculate the sum of each digit raised to the power of the number of digits in the input number.
    # Check if the result is equal to the original number.
    total = 0
    for x in str(num):
        total = total + int(x)**len(str(num))
    return num == total

# Test the function with different numbers and print the results.

for num in range(100, 1000):
    if is_daffodil_num(num):
        print(num)

for num in range(10000, 100000):
    if is_daffodil_num(num):
        print(num)