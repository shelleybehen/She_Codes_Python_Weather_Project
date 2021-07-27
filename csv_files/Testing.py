#pass keyword = don't want to do anything with this now, but wont throw any errors if you leave it blank
#called keeping your code DRY(Don't Repeat Yourself)

# def hello_func(greeting, name = "You"): #def = definition () = parameters variable =only within the function
#     return"{}, {} Function." .format(greeting, name)

#print(hello_func("Hi", name = "Corey"))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ["Math", "Art"]
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)