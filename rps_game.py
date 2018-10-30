# import the random pakage so that we can generate random numbers
from random import randint

#choices is an array => a container that can hold multiple items
#arrays are 0-based -> the first item s 0, the second is 1, etc
choices = ["Rock","Paper","Scissors"]
# make the computer choose a weapon from the choices array at random
player_life = 3
computer_life = 3
computer_choice = choices[randint(0,2)]
player = False

# def win or lose function
def winorlose(status):
	print("Called win or lose function")
	print("************************")
	print("You", status, "! Would you like to play again")
	choice = input(" Y / N: ")

	#reset the lives
	if choice == "Y" or choice =="y":
		# change global variables
		global player_life
		global computer_life
		global player
		global computer





	#set lives for computer and player
		player_life = 3
		computer_life = 3
		computer_choice = choices[randint(0,2)]
		player = False



	elif choice == "N" or choice == "n":
		print("You chose to quit!")
		print("****************")
		exit()

		
#set up our loop
while player is False:
# set player to True by making a selection
	print("===========================")
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
	if player_life == 0:
		print("Your lives: ", player_life)
		print("Computer lives: ", computer_life)
		winorlose("lose")


#set to restart or to quit when game over (computer loses)	
	if computer_life == 0:
		print("Your lives: ", player_life)
		print("Computer lives: ", computer_life)
		winorlose("lose")



	

	
