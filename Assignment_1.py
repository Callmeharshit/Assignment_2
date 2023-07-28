# task 1

# Radius of circle
radius = float(input("Enter the radius: "))
area = 3.141 * radius * radius
print("The area of the circle is:", area, "msq")


# Extension of a file


def get_file_extension(filename):
    
    name, extension = filename.split(".", 1)

    # Print the extension (converted to lowercase)
    print("The extension of the file is:", extension.lower())

# Get the filename from the user
filename = input("Input the Filename: ")

# Call the function to print the extension
get_file_extension(filename)


# I think this will work...?
