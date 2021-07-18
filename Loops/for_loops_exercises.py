#Q1

# user_input = input("Please enter a number ")
# for number in range(int(user_input)):
#     print(f"{user_input} * {number + 1} = {int(user_input) * (number + 1)}")

#Q2

# user_input = input("Please enter a number ")
# for number in range(int(user_input)):
#     print(f"{user_input} * {number + 1} = {int(user_input) * (number + 1)}")

#Q3

# user_input = input("Please enter a number ")
# for number in range(int(user_input)):
#     print(f"{user_input} * {number + 1} = {int(user_input) * (number + 1)}")

#Q4

mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]
for item in mailing_list:
    print(f"{item[0]}: {item[-1]}")


print(f"{mailing_list[0][0]}: {mailing_list[0][-1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][-1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][-1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][-1]}")
print(f"{mailing_list[-1][0]}: {mailing_list[-1][-1]}")
