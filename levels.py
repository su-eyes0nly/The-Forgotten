# LEVELS
#TODO: Figure out how to add level codes so the player can skip to the last level they completed

import enemy 
import items 


class Intro():
	print ("THE FORGOTTEN")

	
class Prelude():
	print ("\nCharacter comes to in an old shack...")
	print ("After a few minutes your vision begins to clear, standing above you is an oddly young looking shaman.")
	print ("Shaman: \"You must have been caught in the storm, I found you passed out in an opening in the forest.\"")
	print ("Shaman: \"You're lucky I found you, I brought you here to rest and heal your wounds.\"")
	print ("\nShaman: \"What is your name traveller?\"")
	player = input("> ")
	print ("My name is %s... Thank you, by the looks of it you saved my life." % player)
	print ("\nShaman: \"So %s. Do you know how you got here?\"" % player)
	print ("%s: \"I have no idea. The last thing I remember was encountering a bear in the forest.\"" % player)
	print ("%s: \"Something spooked the bear and it fled, next thing I knew I woke up hear and...\"" % player )
	print ("%s: \"My gear!? Do you know where it is?\"" % player)
	print ("%s: \"My Grandfather gave me that gun, it's special, extremely rare.\"" % player)


class Forest():
	print ("Do you wish to proceed?")

	option = input ("> ")
	yes = True
	no = False

	if option == "yes":
		print ("You left the company of the Shaman.")
		print ("You stand at the mouth of the forest...")
		if option == "no":
			print ("Coward!")
	else:
		print ("What?")

	def attack(enemy):
		print ("A monster! "+enemy.wolf.name+" ")
	
	
class ForestHeart():
	pass

	
class Labyrinth():
	pass

	
class Graveyard():
	pass

	
class Castle():
	pass

	
class CastleBowels():
	pass


class NextLevel():
	print ("Do you wish to proceed?")

	option = input ("> ")
	yes = True
	no = False

	if option == "yes":
		print ("You left.")
		print ("You stand at...")
		if option == "no":
			print ("Coward!")
	else:
		print ("What?")
