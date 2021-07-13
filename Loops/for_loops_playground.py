#Loops - repetitive tasks
#Loop - for loops , while loops
#For Loops are better to use if you know how many times to repeat a task
#While Loops are better if you don't know how many times to repeat.

#For loops used to iterating over a sequence, strings, lists, dictionaries
#for num in range(5):
 #   print(num)

#for num in range(1,12,2):
#   print(num)

#Use for loop to print numbers
#0 to 100 (inclusive)

#Use for loop to print numbers
#0 to 100 (skip 5) , 0,5,10,15

#for num in range(101):
#   print(num)

#for num in range(0,100,5):
#   print(num)

#chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

#for item in range(len(chilli_wishlist)): #range(4)
#    print(chilli_wishlist[item])
#for item in chilli_wishlist:
#    print(item)

#adapt the for loop to print message
#for each item in the list e.g. "Chilli wants; item"

#Use a for loop to print each item in a list
#from a previous exercise or example

#for item in chilli_wishlist:
#    print(f"Chilli wants {item}")

#names = ["Broooke" , "Carlie", "Katie", "Stacey"]

#for name in names:
#    print(name)

#chilli_wishlist = [
#    ["igloo"],
#    ["donut toy", "tennis ball", "crocodile toy"], #toys
#    ["chicken", "peanut butter"], #food
#    ["cardboard box", "kong", "dig mat"]
#]

#for category in chilli_wishlist:
#    for item in category:
#        print(item)

#While loops
count = 0
while  count < 5: #boolean calculation
    print("hello")
    #count = count + 1
    count += 1