# checks user enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if user don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you did not choose a valid answer")




def instructions():
    print('''
    
    **** INSTRUCTIONS ****
    
    ~write instructions here~
    
    
    ''')

# Main routine
print()
print("          ROLL IT 13        ")
print()

# loop for testing

want_instructions = yes_no("Do you want to read the instructions?")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")

