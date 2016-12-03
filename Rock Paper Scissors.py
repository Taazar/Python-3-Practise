from random import choice
import sys
import getpass

def player_names(player):
    if player == 3:
        return input("Please enter the name you want the computer to have: ")
    else:
        return input("Please enter the name for Player {}: ".format(player))

def game(p1, p2, mode):
    pc, names = [], [p1, p2]
    for i in range(mode):
        while True:
            choices = getpass.getpass("\nPlease enter your choice {}: \n1) Rock. \n2) Paper \n3) Scissors \nPlease enter either '1', '2' or '3': ".format(names[i]))
            if choices not in ["1", "2", "3"]:
                print("That was not a valid choice.")
                continue
            else:
                pc.append(choices)
                break
    if mode == 1:
        pc.append(choice(["1", "2", "3"]))
    beats = {"1": "3", "2": "1", "3": "2"}
    objects = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    if pc[0] == pc[1]:
        print("It's a tie! Both {} and {} chose {}.".format(p1, p2, objects[pc[0]]))
    elif beats[pc[0]] == pc[1]:
        print("{} beats {}! {} wins!".format(objects[pc[0]], objects[pc[1]], p1))
    else:
        print("{} beats {}! {} wins!".format(objects[pc[1]], objects[pc[0]], p2))

def rock_paper_scissors():
    p1, p2, p3 = "Player1", "Player2", "Computer"
    print("Welcome to Rock, Paper, Scissors.")
    while True:
        while True:
            choices = input("\nWhat do you want to do? \n1) Start Game \n2) Change Player Names \n3) Quit Game \nPlease enter either '1', '2' or '3': ")
            if choices not in ["1", "2", "3"]:
                print("You did not enter either '1', '2' or '3'.")
                continue
            else:
                break
        if choices == "3":
            sys.exit()
        elif choices == "2":
            p1 = player_names(1)
            p2 = player_names(2)
            p3 = player_names(3)
            continue
        else:
            while True:
                choices = input("\nWho do you want to play against? \n1) Another Person \n2) The Computer \nPlease enter either '1' or '2': ")
                if choices not in ["1", "2"]:
                    print("You did not enter either '1' or '2'.")
                    continue
                else:
                    break
            if choices == "1":
                game(p1, p2, 2)
            else:
                game(p1, p3, 1)
        continue
##        while True:
##            choices = input("Do you want to play again? \n1) Yes \n2) No \nPlease enter either '1' or '2': ")
##            if choices not in ["1", "2"]:
##                print("You did not enter either '1' or '2'.")
##                continue
##            else:
##                break
##        if choices2 == "1":
##            continue
##        else:
##            sys.exit()

rock_paper_scissors()
