import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#not sure what argument would go here?  
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return (f"{temp}{DEGREE_SYBMOL}")



def convert_date(iso_string):
    weekday = datetime.strptime(iso_string, "%d/%m/%y %H:%M:%S").strftime("%A")
    day = datetime.strptime(iso_string, "%d/%m/%y %H:%M:%S").strftime("%d")
    month = datetime.strptime(iso_string, "%d/%m/%y %H:%M:%S").strftime("%m")
    year = datetime.strptime(iso_string, "%d/%m/%y %H:%M:%S").strftime("%y")
    
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    return(f"{weekday} {day} {month} {year}.")
print(convert_date("2020-06-19T07:00:00+08:00"))


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_c = (temp_in_farenheit - 32) / 1.8
    return temp_in_c
#print(round(convert_f_to_c(100), 1))
    
pass

#how to work out how long list of numbers will be?
def calculate_mean(weather_data):
    # total = a + b
    # mean = total / 2
    # return mean
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

# avg = sum(number_list)/len(number_list)
# print("The average is ", round(avg,2))
    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
