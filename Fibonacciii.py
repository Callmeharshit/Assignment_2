# Fibonacci_Series
def fibonacci(n):
    num = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    
    if n <= 1:
        return num[:n+1]  # Return the sequence up to the given number
    
    for i in range(2, n+1):
        next_fib = num[i-1] +  numi-2]  # Compute the next Fibonacci number
        num.append(next_fib)  # Add the next Fibonacci number to the sequence
    
    return num

# Test the program
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
order_numbers = fibonacci(num_terms)
print("Fibonacci sequence is: ")
print(num)
