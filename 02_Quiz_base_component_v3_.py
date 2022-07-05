import random


# Function used to check input is valid

# Check for an integer more than 0

def num_check(question, low=None, high=None, exit_code = None):
    error = "please enter a whole number between {} and {}\n ".format(low, high)

    while True:

        response = input(question)

        # check to see if response is the exit code and return it
        if response == exit_code:
            return response

        try:

            response = int(response)

            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        # checks input is a integer
        except ValueError:
            continue


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


# prints instructions


def instructions():
    print("                      ++++ How to play ++++              ")
    print()
    print("  --- First you will choose how many Questions you would like .---")
    print()
    print("  --- Then the computer will give you three numbers from which you will pick the highest number. ------  ")
    print()
    print("  --- If you get it wrong the computer will tell you so and the questions will continue and so forth.----   ")
    print()





# list to hold summary / rounds history
game_summary = []


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
# Main routine goes here will start after this
rounds_played = 0
rounds_lost = 0



# Ask user for # of rounds, <enter> for infinite mode

rounds = num_check("How many Questions? ",1 , 100, exit_code="")

print("You have chosen {} Questions".format(rounds))
print()

end_game = "no"
while end_game == "no":

    # Start of game play loop
    number_list = random.sample(range(1, 101), 3)
    random_num = max(number_list)
    rounds_played += 1

    # Rounds Heading
    print()
    rounds == ""
    heading = "Question {} of {}".format(rounds_played, rounds)

    print(heading)
    print(number_list)

    # check the guess was a number between 1 and 100
    guess = num_check("Guess: ", 1, 100, "xxx")

    # end game if exit code is typed
    if guess == "xxx":
        break

    # change guess to an integer
    guess_int = int(guess)
    # rest of loop / game

    # Check the number guessed
    if guess_int == random_num:
        result = "have Correctly Guessed"
    elif random_num > guess_int:
        rounds_lost = +1
        result = "have Incorrectly guessed"
    elif guess_int > random_num:
        rounds_lost = +1
        result = "have Incorrectly guessed"

    # tell user what was guessed.
    print(" You guessed {}".format(guess))

    # prepare to give the user feedback/ for the end of game summary
    feedback = "you {} , the largest number was {}".format(result,random_num)
    outcome = "Question {}: {}".format(rounds_played, feedback)

    print(feedback)
    game_summary.append(outcome)

    # exit games when questions are done
    if rounds_played == rounds:
        break

# defining rounds won
rounds_won = rounds_played - rounds_lost

# **** Calculate Game Statistics ******
# figuring out how many were lost and won.
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("***** Quiz statistics ******")

print()


# displays game stats with % values to the nearest whole number
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%) ".format(rounds_won,
                                                        percent_win,
                                                        rounds_lost,
                                                        percent_lose,
                                                        ))

# Quiz history - questions 1 forwards

print()
print("***** Game History ******")
for game in game_summary:
    print(game)

print()



















#          0000              0000
#        00000000          000000000
#          0000              0000

#             00   00
#               090
#         /                 /
#         //00            00//
#          //00        00//
#          //0000000000//



