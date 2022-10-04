play = " "
while (play == " "):
    player1 = input ("Choose option: (Rock, Paper, Scissors\n ")
    player1 = player1.capitalize()
    player2 = input ("Choose option: (Rock, Paper, Scissors\n ")
    player2 = player2.capitalize()
    
    if (player1 == "Rock"):
        if (player2 == "Rock"):
            print ("Points shared!! draw\n")
        elif (player2 == "Paper"):
            print(f"\n {player2} Wins\n")
        elif (player2 == "Scissors"):
            print(f"\n{player1} Wins\n")
        break
    elif (player1 == "Paper"):
        if (player2 == "Paper"):
            print ("\nPoints are shared!! draw\n")
        elif (player2 == "Rock"):
            print (f"\n{player1} wins\n")
        elif (player2 == "Scissors"):
            print (f"\n{player2} wins\n")
        break
    elif (player1 == "Scissors"):
        if (player2 == "Scissors"):
            print ("\nPoints shared!! draw\n")
        elif(player2 == "Paper"):
            print (f"\n{player1} wins\n")
        elif (player2 == "Rock"):
            print (f"\n{player2} Wins\n")
        break
    else:
        print ("\nSorry invalid input\n")
  
