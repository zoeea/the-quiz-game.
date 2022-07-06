

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

            return response

        # checks input is a integer
        except ValueError:
            continue
