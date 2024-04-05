# Define a function named is_narcissistic_num that takes a number (num) as an argument.
# def is_narcissistic_num(num):
#     # Calculate the sum of each digit raised to the power of the number of digits in the input number.
#     # Check if the result is equal to the original number.
#     return num == sum([int(x) ** len(str(num)) for x in str(num)])

def is_narcissistic_num(num):
    # Calculate the sum of each digit raised to the power of the number of digits in the input number.
    # Check if the result is equal to the original number.
    i = num // 100
    j = num // 10 % 10
    k = num % 10
    return num == i**3 + j**3 + k**3

# Test the function with different numbers and print the results.

for num in range(100, 1000):
    if is_narcissistic_num(num):
        print(num)

# for num in range(1000, 10000):
#     if is_narcissistic_num(num):
#         print(num)