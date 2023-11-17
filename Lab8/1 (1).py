from functools import reduce

def multiply_list(numbers):
    
    result = reduce(lambda x, y: x * y, numbers)
    return result

number_list = [1, 9, 10, 5]
result = multiply_list(number_list)
print(f"The product of the numbers in the list is: {result}")
