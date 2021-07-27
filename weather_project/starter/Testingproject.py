import csv

with open("tests/data/example_one.csv", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    headings = next(csv_reader)
    for row in csv_reader:
        print(row)
