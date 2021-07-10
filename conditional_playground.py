#is_raining = False
#is_cold = True

#print(type(is_raining))
#print(is_cold)
#print(type(is_cold))
#print(is_raining)
#print(not is_raining)
#print(is_raining and is_cold)
#print(is_raining and not is_cold)

#print(is_raining) #f
#print(not is_raining) #t
#print(is_raining or is_cold) #t
#print(is_raining and not is_cold) #f
#print(is_raining or not is_cold) #f
#print(not is_raining and not is_cold) #f

#print(5 < 3) #Just like in maths you would get a false
#print(5 > 3) #t
#print(10 >= 10) #t
#print(4 <= 10) #t
#print(5 == 5) # if 2 vals the same = true if not the same = false
# 1 Equal sign is assiging a variable 2 equals sign is an equality operator
#(x==y) is False because we assigned different values to x and y
#(y==z) is True because we assign equal values to y and z
#print(5 != 4) #!= is not equal to
#print(5.1 > 2.4)
#print("Alisi" =="asli") #false if text is not completely the same it won't be equal
#print("Asli" != "asli")

#temperature = 16
#print(temperature < 18) #true because 16 is less than 18
#wind_chill = 3
#print(wind_chill > 4) #false because 3 is not greater than 4
#print(temperature - wind_chill < 16)

#name = "Hayley"
#print(name == 'Hayley')
#print(name != "Hayley")

#if statements
#is_raining = False
#if
#if is_raining:
#    print("Take an umbrella.")

#if and else
#if is_raining:
#    print("take and umbella.")
#else:
#    print("Do not take an umbrella.")
is_raining = True
temperature = 16
wind_chill = 3
#if temperature - wind_chill < 16:
#    print("Take a jumper.")
#elif temperature - wind_chill > 30:
#    print("Euck, it's hot today, stay inside.")
#else:
#    print("Wow, what a lovely day")
    #nested if statements
if temperature - wind_chill < 5 and is_raining:
    print("Just stay home")
else:
    if is_raining:
        print("You'll need an umbrella today.")
    if temperature - wind_chill < 16:
        print("You'll need a jumper today.")