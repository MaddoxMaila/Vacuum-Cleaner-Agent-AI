

class Environment :

	MAP_OBSTACLE = 'O'
	MAP_ROAD = '-'

	SIZE = 0
	BUMP = False
	SEED = 0

	POS_X = 0
	POS_Y = 0

	ROOM_URL = "A"
	ROOM = []

	def __init__(self):

		pass

	def getRoomURL(self, room):

		if room is 'A':
			self.ROOM_URL = 'map/roomA.txt'

		elif room is 'B':
			self.ROOM_URL = 'map/roomB.txt'

	def loadRoomParams(self, params) :

		self.SIZE = int(params[0])
		self.POS_X = int(params[1])
		self.POS_Y = int(params[2])
		self.DIRTY = params[3]
		self.SEED = params[4]

	def loadRoom(self, room) :

		self.getRoomURL(room) # Sets The ROOM_URL To The Appropriate MAP URL FILE

		try :
			mapFile = open(self.ROOM_URL)  # Open File In URL

			params = [float(x) for x in mapFile.readline().split(' ')]

			self.loadRoomParams(params=params)

		except IOError :

			print("Input Map Not Found")




