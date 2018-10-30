# import the random pakage so that we can generate random numbers
from random import randint

#choices is an array => a container that can hold multiple items
#arrays are 0-based -> the first item s 0, the second is 1, etc
choices = ["Rock","Paper","Scissors"]
# make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0,2)]

#set lives for computer and player
player_life = 3
computer_life = 3

player = False

#set up our loop
while player is False:
# set player to True by making a selection
	print()
	print("Your lives: ", player_life)
	print("Computer lives: ", computer_life)
	print("Choose your weapon !!!")
	player = input("Rock, Paper or Scissors ?\n")

#quit game
	if player == "quit":
		exit()

#choices of player and computer
	print("Player chooses:", player)
	print("Computer chooses: ", computer_choice)
	
#set the restart command
	if player == "restart":
		player_life = 3
		computer_life = 3
		player = False
		computer_choice = choices[randint(0,2)]

#check for a tie = choices are the same
	if player == computer_choice:
		print("Tie! You live to shoot another day")
		
#check to see if the computer choices beats our choices or not
	elif player == "Rock":
		if computer_choice == "Scissors":
			computer_life -= 1
			print("You win !!!", player, "smashes" ,computer_choice)
			
		else:
			player_life -= 1
			print("You lose !!!", computer_choice, "smashes" , player)
			
	elif player == "Scissors":
		if computer_choice == "Paper":
			computer_life -= 1
			print("You win !!!", player, "smashes" ,computer_choice)
		else:
			player_life -= 1
			print("You lose !!!", computer_choice, "smashes" , player)
			

	elif player == "Paper":
		if computer_choice == "Rock":
			computer_life -= 1
			print("You win !!!", player, "smashes" ,computer_choice)
			
		else:
			player_life -= 1
			print("You lose !!!", computer_choice, "smashes" , player)
	
	else:
		print("Check your spelling ...")

#reset the game loop and start over again
	player = False
	computer_choice = choices[randint(0,2)]

#set to restart or to quit when game over (player loses)	
	while player_life == 0:
		print()
		print("Your lives: ", player_life)
		print("Computer lives: ", computer_life)
		print("Game over man, you suck !!!")
		player = input("restart or quit ??\n")
		if player == "restart":
			player_life = 3
			computer_life = 3
			player = False
			computer_choice = choices[randint(0,2)]

		if player == "quit":
				exit()
		else:
			print("Check your spelling ...")


#set to restart or to quit when game over (computer loses)	
	while computer_life == 0:
		print()
		print("Your lives: ", player_life)
		print("Computer lives: ", computer_life)
		print("You are awesome, you beat it")
		player = input("restart or quit ??\n")
		if player == "restart":
				player_life = 3
				computer_life = 3
				player = False
				computer_choice = choices[randint(0,2)]
		if player == "quit":
				exit()
		else:
			print("Check your spelling ...")



	

	
