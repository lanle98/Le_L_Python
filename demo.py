print("Rules that govern the state of water")

#set up a variable to hold the temperature we input
current_temp = True

while current_temp is True:
	#make this a number and clean the code up ( Dry it out )
	current_temp = input(int("Enter a temperature:\n"))
#see what current temp is
	print("your input:", current_temp)

# if the current temp is at freezing or below, water is solid
	if((current_temp) < 0 or (int(current_temp) == 0)):
		print("water is a solid! cuz it's at or below freezing")
		current_temp = True

#else check another condition. If it's not freezing, is below boiling?
	elif((current_temp) < 100):
		print("water is a liquid, because it's above freezing and below boiling")
		current_temp = True

	elif ((current_temp) > 100 or (int(current_temp) == 100)):
		print("water is a gas. Cuz it's, like, really hot")
		current_temp = True
