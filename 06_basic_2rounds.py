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

rounds_played=0

# Ask user for # of rounds, <enter> for infinite mode
rounds = num_check("How many Questions? <enter> for infinite mode")

if rounds == "":
    print("You have chosen infinite mode")
else:
    print("You have chosen {} Questions".format(rounds))
    print()

end_game = "no"
while end_game == "no":
    # Start of game play loop
    number_list = random.sample(range(1, 101), 3)
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

