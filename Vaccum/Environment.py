import random


class Environment:

	ROOM = []
	ROOM_ROWS = 0
	ROOM_COLS = 0
	ROOM_TILE = 0

	DIRTY_TILE = 1
	CLEAN_TILE = 0
	CHILD = 'C'

	def __init__(self, n: int, m: int):

		self.ROOM_ROWS = n
		self.ROOM_COLS = m

	def build_room(self) -> None:

		if self.ROOM_ROWS * self.ROOM_COLS <= 1:

			print("{}*{} > 1 : Your Room/Grid Should be greater than 1".format(self.ROOM_ROWS, self.ROOM_COLS))
			return

		for i in range(0, self.ROOM_ROWS + 1):

			temp_list = []

			for j in range(0, self.ROOM_COLS):

				random_num = random.uniform(0, 1)

				if random_num <= 0.1:   # Imitate 10% chance of the tile becoming dirty
					temp_list.append(self.DIRTY_TILE)
					self.ROOM_TILE = 1
				else:
					temp_list.append(self.CLEAN_TILE)
					self.ROOM_TILE = 0

			self.ROOM.append(temp_list)

	def get_room(self) -> list:
		return self.ROOM

	def set_room(self, room: list) -> None:
		self.ROOM = room

	def get_rows(self) -> int:
		return self.ROOM_ROWS

	def get_cols(self) -> int:
		return self.ROOM_COLS
