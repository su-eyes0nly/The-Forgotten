# items library

class weapon():
	def pistol(self, weapon):
		self.name = "Silver"
		self.dmg = 20
		
	def scythe(self, weapon):
		self.name = "Red Star"
		self.dmg = 20

			
class armor():
	def head (self, armor):
		pass
		
	def chest(self, armor):
		pass
		
	def hands(self, armor):
		pass
		
	def legs(self, armor):
		pass
		
	def boots(self, armor):
		pass
		
class inventory():
	def items():
		pass
	def equip():
		pass
		
	def empty():
		if inventory.items < 1:
			print ("Your inventory is empty")