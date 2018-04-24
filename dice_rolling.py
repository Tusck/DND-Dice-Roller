import random

while True:
    number_of_sides = input('How many sides does your dice have: ')
    try:
        number_of_sides = int(number_of_sides)
        if number_of_sides < 1:
            print('Please choose a postive number')
        else:
            break
    except:
        print('Please choose a positive number')

num_list = []

while True:
    roll = input('Do you want to roll the dice, Y or N: ')
    roll = roll.lower()
    if roll == "n":
        print('Have a nice day!')
        break
    elif roll != 'y':
        print("Choose Y or N")
    else:
        dice_roll = random.randint(1,number_of_sides)
        print(dice_roll)
        num_list.append(dice_roll)

total_roll = sum(num_list)
num_rolls = len(num_list)
if num_list:
    print("You rolled {} times".format(num_rolls))
    print("Your total rolled was: {}".format(total_roll))
    print("Your average role was: {}".format(round(total_roll/num_rolls, 1)))
