"""  #################
     # The Forgotten #
	 #################
"""  
# ENGINE:: game engine
# WORLD:: 
# LEVEL:: 
# CHARACTER:: 
# ACTION:: movement and interaction logic
# ENEMY:: 

# import libraries for game engine
from levels import *
from enemy import *
from items import inventory
import random, sys, time


def start():
	Intro()
	Prelude()
	Forest()