#Here are some Python input methods and string slicing examples:

#Input Methods:

#1. input() - reads input from the user and returns a string

name = input("Enter your name: ")
print("Hello, " + name)


# String Slicing:

# 1. string[start:stop] - returns a slice of the string from start to stop

hello = "Hello, World!"
print(hello[0:5])  # Output: "Hello"

#2. string[start:] - returns a slice of the string from start to the end

hello = "Hello, World!"
print(hello[7:])  # Output: "World!"

#3. string[:stop] - returns a slice of the string from the beginning to stop

hello = "Hello, World!"
print(hello[:5])  # Output: "Hello"

#4. string[-1] - returns the last character of the string

hello = "Hello, World!"
print(hello[-1])  # Output: "!"

#5. string[::step] - returns a slice of the string with a step size of step

hello = "Hello, World!"
print(hello[::2])  # Output: "HloWrd!"

#Note: The :: syntax is called "extended slicing" and allows you to specify a step size.

print("Example:\n")

string = "Hello, World!"
print(string[0:5])  # Output: "Hello"
print(string[7:])  # Output: "World!"
print(string[:5])  # Output: "Hello"
print(string[-1])  # Output: "!"
print(string[::2])  # Output: "HloWrd!"
