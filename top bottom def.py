import random

choices = ["top", "bottom"]
plays = 0
win = 0
lose = 0
tie = 0
player = ''
number_of_computer = 0
computer = 0
def simmilar():
    for number_of_computer in range(1,3):
        print(f"computer {number_of_computer}: {computer1}")
    print(f"player: ", player)
def simmilar1():
    print(f"computer 1: {computer1}")
    print(f"computer 2: {computer2}")
    print(f"computer 3: {computer3}")
    print("player: ", player)

while True:
    plays += 1
    computer1 = random.choice(choices)
    computer2 = random.choice(choices)
    computer3 = random.choice(choices)
    while True:
        number_of_computer = int(input("how many computer you want between 2 or 3?: "))
        if number_of_computer in range(2, 4):# and not str(number_of_computer):
            # number_of_computer[range(number_of_computer)] = random.choice(choices)
            break
        else:
            print("Please give a proper number.")
            continue
    # number_of_computer[range(number_of_computer)] = random.choice(choices)
    while True:
        player = input("top or bottom?: ").lower()
        if player in choices:
            break
    if number_of_computer == 2:
        if player == computer1 == computer2:
            simmilar()
            print("Tie!")
            tie += 1

        elif player == "top":
            if computer1 == computer2 == "bottom":
                simmilar()
                print("You win!")
                win += 1
            if computer1 == "top" and computer2 == "bottom":
                simmilar()
                print("computer 2 win!")
                lose += 1
            if computer1 == "bottom" and computer2 == "top":
                simmilar()
                print("computer 1 win!")
                lose += 1

        elif player == "bottom":
            if computer1 == computer2 == "top":
                simmilar()
                print("You win!")
                win += 1
            if computer1 == "bottom" and computer2 == "top":
                simmilar()
                print("computer 2 win!")
                lose += 1
            if computer1 == "top" and computer2 == "bottom":
                simmilar()
                print("computer 1 win!")
                lose += 1
    elif number_of_computer == 3:
        if player == computer1 == computer2 == computer3:
            simmilar()
            print("Tie!")
            tie += 1

        elif player == "top":
            if computer1 == computer2 == computer3 == "bottom":
                simmilar1()
                print("You win!")
                win += 1
            if computer1 == "top" and computer2 == "bottom" and computer3 == "top":
                simmilar1()
                print("computer 2 win!")
                lose += 1
            if computer1 == "bottom" and computer2 == "top" and computer3 == "top":
                simmilar1()
                print("computer 1 win!")
                lose += 1
            if computer1 == "top" and computer2 == "top" and computer3 == "bottom":
                simmilar1()
                print("computer 3 win!")
                lose += 1

        elif player == "bottom":
            if computer1 == computer2 == "top" == computer3 == "top":
                simmilar1()
                print("You win!")
                win += 1
            if computer1 == "bottom" and computer2 == "top" and computer3 == "bottom":
                simmilar1()
                print("computer 2 win!")
                lose += 1
            if computer1 == "top" and computer2 == "bottom" and computer3 == "bottom":
                simmilar1()
                print("computer 1 win!")
                lose += 1
            if computer1 == "bottom" and computer2 == "bottom" and computer3 == "top":
                simmilar1()
                print("computer 3 win!")
                lose += 1

        elif player == computer1 and computer2 == computer3 or player == computer2 and computer1 == computer3 or player == computer3 and computer2 == computer1:
            tie += 1
            print(f"player: {player}")
            print(f"computer 1: {computer1}")
            print(f"computer 2: {computer2}")
            print(f"computer 3: {computer3}")
            print("its a tieeeeeeeeeeeeeeeeeeeeeeeeeee")
    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break

print(f"you have play {plays} times!! you win {win} times, lose {lose} time and tie {tie} times!!")
if win > lose and tie:
    print("You win most of it!!")
elif lose > win and tie:
    print("You lose most of it!!")
elif tie > lose and win:
    print("You tie most of it!!")
elif win == lose == tie:
    print("You win, lose and tie most of the time!!")