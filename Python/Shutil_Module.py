"""Learning about the shutil module in Python."""

import shutil
import time

# Copying a file using copy()
shutil.copy("Python/images/sea-grass.jpg", "Python/images/grass1.jpg")

# Copying a directory with its file using copytree()
shutil.copytree("Python", "Python_Tutorials")

# Move a file using move()
shutil.move("Python/images/sea-grass.jpg", "Python/sea-grass.jpg")

time.sleep(5)

# Remove a directory with its file using rmtree()
shutil.rmtree("Python_Tutorials")
