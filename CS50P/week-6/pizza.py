import sys
import csv
import os

from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

if not os.path.exists(sys.argv[1]):
    sys.exit("File does not exist")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        rows = list(reader)

    print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")





