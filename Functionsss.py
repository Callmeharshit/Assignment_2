# creating_A_Function
def most_frequent(string):
    my_num = {}

    # Iterate over each character in the string
    for char in string:
        # Increment the count of the current character in the dictionary
        my_num[char] = my_num.get(char, 0) + 1

    # Sort the dictionary by value (frequency) in descending order
    sorted_freq = sorted(my_num.items(), key=lambda x: x[1], reverse=True)

    # Print the letters in decreasing order of frequency
    for char, freq in sorted_freq:
        print(char, "-", freq)


# Test the function
input_string = input("Enter a string: ")
 most_frequent(input_string)   
