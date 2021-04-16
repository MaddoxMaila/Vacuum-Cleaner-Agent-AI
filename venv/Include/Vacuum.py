
class Vacuum :

	LAST_ACTION = None
	POS_X = 0
	POS_Y = 0

	def __init__(self):

		self.dirty = False
		self.bump  = False

	"""
	 Following 6 Methods Are Just For
		:return LAST_ACTION of The Vacuum Cleaner
	"""
	def up(self):
		self.LAST_ACTION = "UP"
		return "UP"

	def down(self):
		self.LAST_ACTION = "DOWN"
		return "DOWN"

	def left(self):
		self.LAST_ACTION = "LEFT"
		return "LEFT"

	def right(self):
		self.LAST_ACTION = "RIGHT"
		return "RIGHT"

	def suck(self):
		self.LAST_ACTION = "SUCK"
		return "SUCK"

	def idle(self):
		self.LAST_ACTION = "IDLE"
		return "IDLE"

	"""
		Args :
			:param Env from Class Environment
	"""
	def see(self, env):

		self.bump = env.bump
		self.dirty = env.dirt_amout(self.posX, self.posY)
		self.POS_X, self.POS_Y = env.positionX, env.positionY