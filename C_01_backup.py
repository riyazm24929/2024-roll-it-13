print("ROLL IT 13")


# loop for testing

while True:
    want_instructions = input("Do you want to read the instructions?").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("you chose yes")
    elif want_instructions == "no" or want_instructions == "n":
        print("you chose no")
    else:
        print("you did not choose a valid answer")