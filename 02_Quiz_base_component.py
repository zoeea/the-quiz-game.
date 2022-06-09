import random


# Function used to check input is valid

# Check for an integer more than 0

def num_check(question, high):
    error = "please enter a whole number between 1 and 10 \n "

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if 0 < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()

# Generate 3 random numbers between 1 and 1000

# prints instructions


def instructions():
    print()
    print("  --- First you will choose how many Questions you would like or press <enter> for infinite Questions.---")
    print()
    print("  --- Then the computer will give you three numbers from which you will pick the highest number. ------  ")
    print()
    print("  --- If you get it wrong the computer will tell you so and the questions will continue and so forth.----   ")
    print()


# start of game !!!!!

print()
print("   Welcome to this Game!  ")
print()

# ask user if they need instructions...
played_before = choice_checker("Have you played this Quiz before? ", ["yes", "no"], "Please enter yes or no")
print()

if played_before == "no":
    instructions()

# set game parameters
# How many rounds , or infinite mode
# Main routine goes here....
rounds_played = 0

# Ask user for # of rounds, <enter> for infinite mode

rounds = num_check("How many Questions? <enter> for infinite mode",10)

if rounds == "":
    print("You have chosen infinite mode")
else:
    print("You have chosen {} Questions".format(rounds))
    print()

end_game = "no"
while end_game == "no":

    # Start of game play loop
    number_list = random.sample(range(1, 1001), 3)
    random_num= max(number_list)
    rounds_played += 1

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode:"
        "Round {}".format(rounds_played)

    else:
        heading = "Question {} of {}".format(rounds_played, rounds)

    print(heading)
    print(number_list)
    guess = input("Guess: ")


    # end game if exit code is typed
    if guess == "xxx":
        break


    # rest of loop / game
    print("You guessed {}".format(guess))

    if int(guess) == random_num:
        print("You have guessed the correct number")
    elif random_num > int(guess):
        print("You have guessed wrong")
    elif int(guess) > random_num :
        print("You have guessed the wrong number ")

    # exit games when questions are done
    if rounds_played == rounds:
        break


        # end game if required


# end of game summaruy









#          0000              0000
#        00000000          000000000
#          0000              0000

#             00   00
#               090
#          /                 /
#          //00            00//
#           //00        00//
#           //0000000000//



