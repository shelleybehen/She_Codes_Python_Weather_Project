# #Q1 

# import csv

# with open("colours_20_simple.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for row in csv_reader:
#         print(f"{row[1]} {row[2]} {row[4]}")

#Q2

# import csv

# with open("colours_20_simple.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         print(f"{row[-1]}, Hex:{row[1]}, RGB: {row[0]}")

#Q3

import csv

with open("colours_20.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    headings = next(csv_reader)
    for row in csv_reader:
        print(f"{row[4]}, Hex: {row[2]}, RGB: {row[1]}")
