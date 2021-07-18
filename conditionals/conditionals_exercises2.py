moths_in_house = True
mitch_is_home = True
if moths_in_house and mitch_is_home:
    print("Hoooman!  Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meoooooow!  Hissss!")
elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch.")