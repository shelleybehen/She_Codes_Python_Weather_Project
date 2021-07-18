light_colour = "Red"
car_detected = True

if light_colour and not car_detected:
    print("Do nothing.")
if light_colour and car_detected:
    print("Flash!")
else:
    print("Do nothing.")