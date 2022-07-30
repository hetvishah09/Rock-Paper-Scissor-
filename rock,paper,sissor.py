import random

choices=["rock","paper","scissors"]
computer=random.choice(choices)
player = None

while player not in choices:
    player= input("rock , paper , or scissors?: ")

if player==computer:
    print("computer: ",computer)
    print("player: ",player)
    print("Tie!")


elif player == "rock":
    if computer == "paper":
        print("computer: ",computer)
        print("player: ",player)
        print("you loose!")
    if computer == "scissors":
        print("computer: ",computer)
        print("player: ",player)
        print("you win!")

elif player == "paper":
    if computer == "rock":
        print("computer: ",computer)
        print("player: ",player)
        print("you winp!")
    if computer == "scissors":
        print("computer: ",computer)
        print("player: ",player)
        print("you loose!")

elif player == "scissors":
    if computer == "paper":
        print("computer: ",computer)
        print("player: ",player)
        print("you win!")
    if computer == "rock":
        print("computer: ",computer)
        print("player: ",player)
        print("you loose!")