import csv

# with open("2016_pilbara.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

with open("2016_pilbara.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)


population = []
with open("2016_pilbara.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        population.append(line)
        print(population)
        print()

for age_group in population:
    print(f"{age_group[0]} {age_group[1]}")