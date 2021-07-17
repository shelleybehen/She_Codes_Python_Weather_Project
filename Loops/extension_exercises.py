size = int(input("Pyramid size: "))

result = ""

for i in range(0,size): #start from 0 goes through 5 times
    if size == 1:
        print("*")
    else:
        result = result + "**"
        print("*")

