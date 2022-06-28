import random

# Function used to check input is valid

# Check for an integer more than 0


def num_check(question):
    while True:
        response = input(question).lower()

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0 "

        if response == "" or response =="xxx":
            return response

        else:
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def check_rounds():
    while True:

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n "

        # if infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # if response is too low, go bak to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # if response is not an integer go back to
            # start of loop
            except ValueError:
                print(round_error)
                continue
        
        return response


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


def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

#Generate 3 random numbers between 1 and 1000
random.list = random.sample(range(1, 1000), 3)


# prints instructions

def instructions():
    print()
    print("  * First you will choose how many rounds you would like to play or press <enter> for infinite mode.   ")
    print("  * Then the computer will give you three numbers from which you will pick the highest number.   ")
    print("  * If you get it wrong the computer will tell you so and the rounds will continue and so forth.   ")
    print()

# start of game !!!!!

print()
print("   Welcome to this Game!  ")        
print()

# ask user if they need instructions...
played_before = choice_checker("Have you played the game before? ", ["yes", "no"], "Please enter yes or no")
print()

if played_before == "no":
    instructions() 

# set game parameters 
# How many rounds , or infinite mode
# Main routine goes here....
rounds_played = 0

secret = random.choice(random.list)

# Ask user for # of rounds, <enter> for infinite mode
rounds = num_check("How many rounds? <enter> for infinite mode")

if rounds == "":
    print("You have chosen infinite mode")
else:
    print("You have chosen {} rounds".format(rounds))
    print()

end_game = "no"
while end_game == "no":
    # Start of game play loop

    rounds_played += 1

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode:"
        "Round {}".format(rounds_played)

    else:
        heading = "Rounds {} of {}".format(rounds_played, rounds)

    print(heading)
    print(random.list)
    guess = input("Guess: ")

    # end game if exit code is typed
    if guess == "xxx":
        break
    elif rounds_played == rounds:
        break

    # rest of loop / game
    print("You guessed {}".format(guess))


    if guess == secret:
        print("You have guessed correct")
    elif guess != secret:
        print("You have guessed the wrong number")


# end game if required
    
    
    
    
    