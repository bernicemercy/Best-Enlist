import random
u = 0
c = 0
while True:
    user = input("Enter the input (rock/paper/scissor) : ")
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    print("you chose ",user,"\ncomputer chose ",computer)
    if(user == computer):
        print("It is a tie!")
    elif(user == 'rock' ):
        if(computer == 'scissors'):
            print("Rock smashes scissors!!!. You won!!!")
            u +=1
        else:
            print("ohooo!!! paper covers the rock. you lost!")
            c+=1
    elif user == 'paper':
        if(computer == 'rock'):
            print("Paper covers the rock!! you won!!!")
            u +=1
        else:
            print("ohooo!!! Scissors cut paper... You lost!!")
            c +=1
    elif(user == 'scissors'):
        if(computer == 'paper'):
            print("Scissors cut paper!!! you won!!!")
            u +=1
        else:
            print("Ohoo!!! Rock smashes scissors... you lost!!!")
            c += 1
    else:
        print("Wrong Input...")

    print("\n--------------------------------------------------------------------\n")

    play = input("Play again?? (y/n)")

    if(play.lower()!='y'):
        print("user    Computer\n",u,"        ",c)
        if(u>c):
            print("Hurray!!! you won!!!!")
        elif(c>u):
            print("Better luck next time!!!")
        else:
            print("It is a tie... Well done")
        print("\nThanks for playing ")
        break
