import random


class Environment:

	"""
	Class To Build And Keep Details Concerning The Environment
	"""

	"""
	Vars That Make The Environment
	"""
	ROOM = []
	ROOM_ROWS = 0
	ROOM_COLS = 0
	ROOM_TILE = 0

	"""
	Details Regarding The Environment
	"""
	DIRTY_TILE = 1
	CLEAN_TILE = 0
	CHILD = 'C'

	def __init__(self, n: int, m: int):

		"""
		Constructor
		:param n: Rows
		:param m: Columns
		"""

		self.ROOM_ROWS = n
		self.ROOM_COLS = m

	def build_room(self) -> None:

		"""
		Build The Room
		:return: None
		"""
		if self.ROOM_ROWS * self.ROOM_COLS <= 1:

			print("{}*{} > 1 : Your Room/Grid Should be greater than 1".format(self.ROOM_ROWS, self.ROOM_COLS))
			return None

		"""
		Build The Rows
		"""
		for i in range(0, self.ROOM_ROWS):

			temp_list = []  # Holds The Columns

			for j in range(0, self.ROOM_COLS):

				random_num = random.uniform(0, 1)   # Generate number between 0 & 1

				if random_num <= 0.1:   # Imitate 10% chance of the tile becoming dirty
					temp_list.append(self.DIRTY_TILE)
				else:
					temp_list.append(self.CLEAN_TILE)

			self.ROOM.append(temp_list)  # Add Columns To Rows

	def get_room(self) -> list:

		"""
		:return: return an N*M Room
		"""
		return self.ROOM

	def set_room(self, room: list) -> None:

		"""
		:param room: an N*M room
		:return: None
		"""
		self.ROOM = room

	def get_rows(self) -> int:

		"""
		:return: Number Of Rows
		"""
		return self.ROOM_ROWS

	def get_cols(self) -> int:

		"""
		:return: Number Of Columns
		"""
		return self.ROOM_COLS
