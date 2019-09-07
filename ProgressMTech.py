unit_1 = int(input("Enter how many assignment you have done in unit 1:  "))
unit_2 = int(input("Enter how many assignment you have done in unit 2:  "))
unit_3 = int(input("Enter how many assignment you have done in unit 3:  "))
unit_4 = int(input("Enter how many assignment you have done in unit 4:  "))
unit_5 = int(input("Enter how many assignment you have done in unit 5:  "))
unit_6 = int(input("Enter how many assignment you have done in unit 6:  "))


hours_1 = unit_1 * 3
hours_2 = unit_2 * 3
hours_3 = unit_3 * 3
hours_4 = unit_4 * 3
hours_5 = unit_5 * 3
hours_6 = unit_6 * 3

progress_1 = hours_1 / 15 * 100
progress_2 = hours_2 / 15 * 100
progress_3 = hours_3 / 15 * 100
progress_4 = hours_4 / 15 * 100
progress_5 = hours_5 / 15 * 100
progress_6 = hours_6 / 15 * 100

print("This is your progress in each unit: ")

if unit_1 >= 0 and unit_1 <= 5:
    print("Your progress in unit 1 is: ", progress_1, "%")
else:
    print("You must choose a number between 0 and 5 for unit 1")
if unit_2 >= 0 and unit_2 <= 5:
    print("Your progress in unit 2 is: ", progress_2, "%")
else:
    print("You must choose a number between 0 and 5 for unit 2")
if unit_3 >= 0 and unit_3 <= 5:
    print("Your progress in unit 3 is: ", progress_3, "%")
else:
    print("You must choose a number between 0 and 5 for unit 3")
if unit_4 >= 0 and unit_4 <= 5:
    print("Your progress in unit 4 is: ", progress_4, "%")
else:
    print("You must choose a number between 0 and 5 for unit 4")
if unit_5 >= 0 and unit_5 <= 5:
    print("Your progress in unit 5 is: ", progress_5, "%")
else:
    print("You must choose a number between 0 and 5 for unit 5")
if unit_6 >= 0 and unit_6 <= 5:
    print("Your progress in unit 6 is: ", progress_6, "%")
else:
    print("You must choose a number between 0 and 5 for unit 6")

input("Press the key to quit")





















