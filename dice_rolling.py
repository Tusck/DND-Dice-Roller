import random

number_of_sides = input('How many sides does your dice have: ')
num_list = list()
roll = 'y'
while True:
    try:
        roll = input('Do you want to roll the dice, Y or N: ')
        roll = roll.lower()
        if roll == "n":
            print('Have a nice day!')
            break
        if roll != 'y':
            print("Choose Y or N")
            continue
        if roll == "y":
            dice_roll = random.randint(1,int(number_of_sides))
            print(dice_roll)
            num_list.append(dice_roll)
    except:
        print('Choose Y or N')
        continue

x = sum(num_list)
y = len(num_list)
if y > 0:
    print("You rolled {} times".format(y))
    print("Your total rolled was: {}".format(x))
    print("Your average role was: " + str(x/y))
