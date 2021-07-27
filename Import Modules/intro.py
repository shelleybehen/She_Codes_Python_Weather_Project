#import my_module as mm
# import random #standard library module
#import math = allows us to use standard math e.g. sin, radians etc
#rads = math.radians(90)
#print(math.sin(rads))
# import datetime #allows us to work with dates and times
# import calendar 

# today = datetime.date.today()
# print(today) #gives us todays date
# print(calendar.isleap(2017))

# from my_module import find_index, test  #only gives access to find index fn not everything else in module
# import sys # where python looks when it imports
#courses = ["History", "Math", "Physics", "CompSci"]
#Have to type module name first, then what we want to grab from that module
# index = find_index(courses, "Math")
# print(index)
# print(test)
#print(sys.path) where python imports from
# random_course  = random.choice(courses)
# print(random_course)
import os #gives us access to the underlying operating system
#print(os.getcwd()) #current working directory
print(os.__file__) #prints location of file in our file system