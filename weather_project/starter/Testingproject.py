import csv
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    mini =  min(weather_data)
    minpos = weather_data.index(min(weather_data))
    return(mini , minpos)
print(find_min[49, 57, 56, 55, 53])