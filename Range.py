def print_positive_numbers(numbers_list):
    positive_numbers = [num for num in numbers_list if num > 0]
    print(positive_numbers)

# User input for list1
input_str = input("Enter a list of numbers separated by spaces: ")
list1 = [int(num) for num in input_str.split()]

print("Input:", list1)
print("Output:", end=" ")
print_positive_numbers(list1)

# User input for list2
input_str = input("\nEnter another list of numbers separated by spaces: ")
list2 = [int(num) for num in input_str.split()]

print("Input:", list2)
print("Output:", end=" ")
print_positive_numbers(list2)
