#chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
#if "tennis ball" in chilli_wishlist:
#    print("Chill would like a tennis ball")
#else:
#    print("Chilli doesn't feel like playing today")

#chilli_wishlist.append('dig mat')
#chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy'])
#chilli_wishlist.pop()
#print(chilli_wishlist)
#indexing
#print(len(chilli_wishlist)) #len = number of items in container
#print(chilli_wishlist)
#print(type(chilli_wishlist)) #type = class

#print(chilli_wishlist[0])
#print(chilli_wishlist[1])
#print(chilli_wishlist[-1])
#print(chilli_wishlist[0:2])
#print(chilli_wishlist[1:3])


#print sublist of items in positions 2 through 3 [2] [3]
#print the item in -3
#change the value of the first item in the list

#print(chilli_wishlist[-3])
#print(chilli_wishlist[2:5])
#chilli_wishlist[0] = "strawberry"
#print(chilli_wishlist)
chilli_wishlist = [
    ["igloo"],
    ["donut toy", "tennis ball", "crocodile toy"],
    ["chicken", "peanut butter"],
    ["cardboard box", "box", "dig mat"]
]
print(len(chilli_wishlist))
print(chilli_wishlist[2][0]) #if you want the element itself, drill down one more
print(chilli_wishlist[-1][-1])
