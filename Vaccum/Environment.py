import random

class Environment:

	ROOM = []
	ROOM_ROWS = 0
	ROOM_COLS = 0
	ROOM_TILE = 0

	DIRTY_TILE = 1
	CLEAN_TILE = 0
	CHILD = 'C'

	def __init__(self, n, m):

		self.ROOM_ROWS = n
		self.ROOM_COLS = m

	def build_room(self):

		for i in range(0, self.ROOM_COLS + 1):

			temp_list = []

			for j in range(0, self.ROOM_ROWS + 1):

				random_num = random.uniform(0, 1)

				print(random_num)

				if random_num >= 0.1:   # Imitate 10% chance of the tile becoming dirty
					temp_list.append(self.DIRTY_TILE)
					self.ROOM_TILE = 1
				else:
					temp_list.append(self.CLEAN_TILE)
					self.ROOM_TILE = 0

				print(self.ROOM_TILE)

			self.ROOM.append(temp_list)

	def get_room(self):
		return self.ROOM

	def get_rows(self):
		return self.ROOM_ROWS

	def get_cols(self):
		return self.ROOM_COLS
