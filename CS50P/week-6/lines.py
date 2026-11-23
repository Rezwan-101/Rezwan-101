import sys
import os

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

if not os.path.isfile(filename):
    sys.exit("File does not exist")

count = 0

with open(filename, "r") as file:
    for line in file:
        if line.lstrip().startswith("#"):
            continue

        if line.strip() =="":
            continue


        count += 1


print(count)


