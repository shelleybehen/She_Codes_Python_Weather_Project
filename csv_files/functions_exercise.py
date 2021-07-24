
#Q1 Write a function that takes a temperature in fahrenheitand returns the temperature in celsius

# def convert_ft_to_c(temp_ft):
#     temp_in_c = (temp_ft - 32) / 1.8
#     return temp_in_c

# print(convert_ft_to_c(350))

#Q2 

# def is_odd(num):
#     if float(num) % 2 == 0:
#         return False
#     else:
#          return True
    
# print(is_odd(10))

#Q3

# number_list = [10, 5, 6]
# avg = sum(number_list)/len(number_list)
# print("The average is ", round(avg,2))

#Q4

def multiply_values(price_per_unit,num_units):
    total = price_per_unit * num_units
    return total

print(f"${multiply_values(4.25, 3)}")