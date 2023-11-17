import time
import math

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000.0)

    result = math.sqrt(number)
    
    return result

try:
    number_input = float(input("Enter a number: "))
    
    delay_input = int(input("Enter delay in milliseconds: "))
    
    result = delayed_square_root(number_input, delay_input)
    
    print(f"Square root of {number_input} after {delay_input} milliseconds is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number and delay.")
