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
#     headings = next(csv_reader)
#     for row in csv_reader:
#         print(f"{row[-1]}, Hex:{row[1]}, RGB: {row[0]}")

#Q3

# import csv

# with open("colours_20.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     headings = next(csv_reader)
#     for row in csv_reader:
#         print(f"{row[4]}, Hex: {row[2]}, RGB: {row[1]}")

# #Q4
import csv
red_count = 0
green_count = 0
blue_count = 0
yellow_count = 0
with open("colours_213.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for column in csv_reader:
            if "red" in column[4]:
                red_count += 1
            if "green" in column[4]:
                green_count += 1
            if "blue" in column[4]:
                blue_count += 1
            if "yellow" in column[4]:
                yellow_count += 1
    print(f"Red: {red_count}")
    print(f"Green: {green_count}")
    print(f"Blue: {blue_count}")
    print(f"Yellow: {yellow_count}")
#Q5
# import csv

# with open('galaxies.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     slow = [None, float('inf')]
#     fast = [None, 0]
#     for i, row in enumerate(csv_reader):
#         if i != 0:
#             if int(row[1]) < slow[1]:
#                 slow =  [row[0], int(row[1])]
#             if int(row[1])> fast[1]:
#                 fast = [row[0], int(row[1])]
#     print(f'Galaxy {slow[0]} has a min velocity of {slow[1]}km/sec.')
#     print(f'Galaxy {fast[0]} has a max velocity of {fast[1]}km/sec.')