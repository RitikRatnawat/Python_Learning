"""Learning about the Regular Expressions in Python"""

import re

if __name__ == "__main__":

    TEXT = "The rain in Spain and The tower in Spain"
    print()

    # Searching for a match anywhere in the string.
    PATTERN = "\\s.{3}in\\s"
    result = re.search(PATTERN, TEXT)
    print(result)

    # Getting Data from match Object
    print(result.span())
    print(result.group())

    # Searching for a list of matched values
    PATTERN = "\\sin\\s"
    result = re.findall(PATTERN, TEXT)
    print(result)

    # Splitting a String based on a PATTERN
    PATTERN = "\\sin\\s"
    result = re.split(PATTERN, TEXT)
    print(result)

    # Substitute the value based on a PATTERN
    result = re.sub("\\s", "-", TEXT)
    print(result, "\n")