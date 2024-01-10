import re

# creating a calculator

print("Welcome to CALCULATOR World!")
print("To exit type quit")

previous = 0
run = True


def calculator():
    global run
    global previous

    if previous == 0:
        equ = input("Enter your equation:")
    else:
        equ = input(str(previous))

    if equ == "quit":
        print("Thank you,Bye.")
        run = False
    else:
        equ = re.sub('[a-zA-Z,.:()]', '', equ)

        if previous == 0:
            previous = eval(equ)
            print("Continue:")

        else:
            previous = eval(str(previous) + equ)


while run:
    calculator()
