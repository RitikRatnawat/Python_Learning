"""Learning about the File IO Operations in Python."""

# Reading a File
with open("myfile.txt", "r", encoding="utf-8") as file:
    data = file.read()
    # data = file.readline()
    # data = file.readlines()
    print(data)
    
# Writing a File
with open("myfile.txt", "w", encoding="utf-8") as file:
    file.write("One Line\nTwo Line\nThree Line")
    # file.writelines(["One Line", "Two Line", "Three Line"])
    
# Appending to a File
with open("myfile.txt", "a", encoding="utf-8") as file:
    file.write("\nFour Line")
    
# Seeking and Teling in a File
with open("myfile.txt", "r", encoding="utf-8") as file:
    # Move to 10th byte of the file
    file.seek(10)
    
    # Get Current Position
    print(file.tell())
    
    # Read a 5 bytes from file
    data = file.read(5)
    print(data)
    
    # Now Current Position
    print(file.tell())
    
# Truncate the File
with open("myfile.txt", "a+", encoding="utf-8") as file:
    file.truncate(8)
    file.seek(0)
    print(file.read())
    
    
    
