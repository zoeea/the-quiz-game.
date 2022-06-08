import random


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
    guess = input("Guess: ")  # replace with call to number checking function

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
