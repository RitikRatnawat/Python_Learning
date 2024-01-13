"""Learning about the OS module in the Python."""

# Resource https://docs.python.org/3/library/os.html

import os

# Create a New Directory
if not os.path.exists("data"):
    os.mkdir("data")

for i in range(1, 50):
    if not os.path.exists(f"data/Day{i}"):
        os.mkdir(f"data/Day{i}")

# Renaming the Directories
for i in range(1, 50):
    os.rename(f"data/Day{i}", f"data/Day-{i}")
    
    
# Listing the Directories
print(os.listdir("data"))

# Run a Command in the Terminal
os.system("date")

# Print Current working directory
print(os.getcwd())

# Change Working Directory
os.chdir("/Users/ritikratnawat786/Desktop/Training_Projects/Python_Learning")
print(os.getcwd())

# Remove Directories
for i in range(1, 50):
    os.rmdir(f"Python/data/Day-{i}")
os.rmdir(f"Python/data")