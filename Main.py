from Game import *

if __name__ == '__main__':

    man = Player('Francis')
    machine = Machine()
    referee = Scorer()

    while True:
        your_choice = int(input("Enter [1] for Paper,[2] For Scissor and [3] for Rock"))

        man.setChoice(your_choice)
        machine.choose()

        my_choice = machine.getChoice()

        referee.result(your_choice, my_choice)





