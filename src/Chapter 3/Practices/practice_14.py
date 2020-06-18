"""
eliminate the extra newline character at the end of each line.
"""

filename = input("Please enter the name of a file: ")  # Use texts/file.txt for example
catfile = open(filename, "r")
for line in catfile:
    print(line.rstrip())
catfile.close()
