# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello"
s1 = "Hello"
s2 = 'Hello'
print(f"Strings = {s1} -> {s2} \n")


# Multiline Strings
s3 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(f"Multiline String = {s3}", "\n")


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
s4 = "Hello World!"
print("Accessing elements using Indices")
print(s4[0])
print(s4[2])
print(s4[6])
print(s4[8], "\n")


# Looping through String
s5 = "banana"
print("Looping over String")
for ch in s5:
    print(f"{ch}", end=" -> ")
print("\n")


# String Length - To get the length of a string, use the len() function.
s6 = "Hello World!"
print(f"Length of String '{s6}' = {len(s6)}")


# Check String - To check if a certain phrase or character is present in a string, we can use the keyword "in".
s7 = "The best things in life are free!"
print(f"Is 'free' is present in '{s7}' = {'free' in s7}")
print(f"Is 'paid' is present in '{s7}' = {'paid' in s7}")

# with IF statement
if 'free' in s7:
    print("Yes, 'free' is present \n")
    

# Check if NOT - To check if a certain phrase or character is NOT present in a string, we can use the keyword "not in".
s8 = "The best things in life are free!"
print(f"Is 'free' is not present in '{s8}' = {'free' not in s8}")
print(f"Is 'paid' is not present in '{s8}' = {'paid' not in s8}")

# with IF statement
if 'paid' not in s8:
    print("Yes, 'paid' is not present")