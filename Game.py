import random


class Scorer:

    def __init__(self):

        #  Dictionary that represents the three possible choices
        self.Choices = {1: "Paper", 2: "Scissors", 3: "Rock"}

        self.score = 0
        self.comp_score = 0
        self.man_score = 0

    def addOneToMan(self):
        self.man_score += 1

    def addOneToComputer(self):
        self.comp_score += 1

    def getManScore(self):
        return self.man_score

    def getCompScore(self):
        return self.comp_score

    def result(self, manChoice, machineChoice):
        print("Your choice :" , self.Choices.get(manChoice) ,"\n My Choice :" , self.Choices.get(machineChoice) + "\n")

        # Result
        # {1: "Paper", 2: "Scissors", 3: "Rock"}
        if manChoice == machineChoice:
            print("Both are Same\n")

        elif manChoice == 1 and machineChoice == 2:
            # Man = Paper , Machine = Scissors ====> Machine Wins
            print("You Lost\n")

        elif manChoice == 2 and machineChoice == 1:
            # Man = Scissors , Machine = Paper ====> Man Wins
            print("You Won\n")

        elif manChoice == 1 and machineChoice == 3:
            # Man = Paper , Machine = Rock ====> Man Wins
            print("You Won\n")

        elif manChoice == 3 and machineChoice == 1:  # Machine wins
            # Man = Rock , Machine = Paper ====> Machine Wins
            print("You Lost\n")

        elif manChoice == 2 and machineChoice == 3:  # Scissors and Rock === Machine wins
            # Man = Scissors , Machine = Rock ====> Man Wins
            print("You Lost\n")

        else:
            # Man = Rock , Machine = Scissors ====> Man Wins
            print("You Won\n")


class Machine:

    def __init__(self):
        self.name = "System"
        self.choice = 0

    def choose(self):
        # Returns a random number between 1 and 3
        self.choice = random.randint(1, 3)
        return self.choice

    def getChoice(self):
        return self.choice


class Player:

    def __init__(self, name):
        self.name = name
        self.choice = 0

    def getChoice(self):
        return self.choice

    def setChoice(self, choice):
        self.choice = choice
