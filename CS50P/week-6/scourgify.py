import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Two few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Two many command-line arguments")

try:
    with open(sys.argv[1], newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

except OSError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames = ["first", "last", "house"]

    )

    writer.writeheader()


    for row in rows:
        last, first = row["name"].split(", ")

        writer.writerow({
            "first": first,
            "last": last,
            "house": row["house"]
        })


