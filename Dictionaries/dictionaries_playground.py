groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
    }
#look at a specific value
# print(groceries["Baby Spinach"])

#Add an item
groceries["Avocados"] = 1.00
# print(groceries)
#remove an item
del groceries["Bacon"]
# print(groceries)

#iterating over the dictionary
for item in groceries:
    print(f"{item}: ${groceries[item]}")
print()
# another way to iterate over the dictionary Prettier
# for item, price in groceries.items():
#     print(f"{item}: ${price}")

#another way to iterate over the dictionary
for item, price in groceries.items():
    print(f"{item}: ${price}")
