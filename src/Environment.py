import random

class Environment:

	ROOM = []
	ROOM_ROWS = 0
	ROOM_COLS = 0
	ROOM_TILE = 0

	def __init__(self, n, m):

		self.ROOM_ROWS = n
		self.ROOM_COLS = m

	def build_room(self):

		for i in range(0, self.ROOM_COLS + 1):

			for j in range(0, self.ROOM_ROWS + 1):

				temp_list = []
				random_num = random.uniform(0, 1)

				if random_num >= 0.1:
					self.ROOM_TILE = 1
				else:
					self.ROOM_TILE = 0

				temp_list.append(self.ROOM_TILE)
				self.ROOM.append(temp_list)

	def get_room(self):
		return self.ROOM

	def get_row(self):
		return self.ROOM_ROWS

	def get_cols(self):
		return self.ROOM_COLS
