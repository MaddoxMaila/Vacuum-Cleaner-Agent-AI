from Vaccum.Environment import Environment
import math
import time


class VacuumCleaner:

	"""
		Class VacuumCleaner Provides Functionality A Vacuum Cleaner Show Have
		-> Move Around An N*M Room
		-> Clean Room
		-> Detect Dirt In Room
		-> Keep Position Of It's Current & Last Dirty Tile
	"""

	"""
		Class Level Vars To Keep Track Of The Room
		ROOM_GRID Is The N*M Room The Vacuum Works on
		ROOM_ROW Is Row Of The Room
		ROOM_COLS Is Column Of The Room
	"""
	ROOM_GRID = []
	ROOM_ROWS = 0
	ROOM_COLS = 0

	"""
		Class Level Vars To Keep Position Of Vaccum
		N_POS_X & N_POS_Y Keep Current Vacuum Position
		L_POS_X & L_POS_Y Keep Position Of Last Dirty Tile
	"""
	N_POS_X = 0
	N_POS_Y = 0
	L_POS_X = 0
	L_POS_Y = 0

	"""
		Vars To Keep Performance Metrics
		ROOM_TILES_CLEANED keeps number of tiles cleaned by the Vacuum
		DIRTY_TILES_DISTANCES keeps distances between dirty tiles
	"""
	ROOM_TILES_CLEANED = 0
	DIRTY_TILES_DISTANCES = []

	"""
		Time Vars
	"""
	START_TIME = 0
	END_TIME = 0

	def __init__(self, grid_rows, grid_cols):

		"""
		:param grid_rows: Rows Of The Room
		:param grid_cols: Columnns Of The Room
		"""

		self.ROOM_COLS = grid_cols
		self.ROOM_ROWS = grid_rows

	def show_pos(self, where) -> None:

		"""
		:param where: name of method that called this method, its for debuggin purposes
		:return: None
		"""
		print("{} :=> (x = {}, y = {})".format(where, self.N_POS_X, self.N_POS_Y))

	def get_time(self) -> dict:

		"""
		:return: start & end times of the Vacuum
		"""
		return {"start": self.START_TIME, "end": self.END_TIME}

	def move_horizontal_and_vertical(self) -> str:

		"""
		Give The Vacuum The Ability To Move Around The Room
		:return: None
		"""
		if 0 <= self.N_POS_X <= self.ROOM_ROWS:  # Will Change The Vacuum Direction To Move From Left To Right
			self.right()

		if self.N_POS_X is self.ROOM_ROWS and self.N_POS_Y <= self.ROOM_COLS:
			self.down()
			self.N_POS_X = 0

		return 'Move'

	def right(self) -> None:

		"""
		Move Vacuum Right
		:return: None
		"""
		if self.N_POS_X is not self.ROOM_ROWS:
			self.N_POS_X += 1   # Move The Vacuum Right

	def left(self) -> None:

		"""
		Move Vacuum Left
		:return: None
		"""

		if self.N_POS_X is not self.ROOM_ROWS:
			self.N_POS_X -= 1   # Move The Vacuum Left

	def up(self) -> None:

		"""
		Move Vacuum Up
		:return: None
		"""
		if self.N_POS_Y is not 0 or self.N_POS_Y is not self.ROOM_COLS:
			self.N_POS_Y -= 1

	def down(self) -> None:

		"""
		Move Vacuum Down
		:return: None
		"""
		if self.N_POS_Y is not 0 or self.N_POS_Y is not self.ROOM_COLS:
			self.N_POS_Y += 1

	def set_position_val(self, val) -> None:

		"""
		:param val: Value to be set at the current position
		:return: None
		"""
		self.ROOM_GRID[self.N_POS_X][self.N_POS_Y] = val

	def get_position_val(self) -> int:

		"""
		:return: Return value at the current index
		"""
		if len(self.ROOM_GRID) is 0:
			return 0
		return self.ROOM_GRID[self.N_POS_X][self.N_POS_Y]

	def get_dirty_distances(self) -> list:

		"""
		:return: List containing number of distances between dirty tiles
		"""
		return self.DIRTY_TILES_DISTANCES

	def get_tiles_cleaned(self) -> int:

		"""
		:return: Number of tiles cleaned by the vacuum
		"""
		return self.ROOM_TILES_CLEANED

	def calculate_distance(self) -> None:

		"""
		Calculate distance between two dirty tile using the Euclidian Space Formula
		:return: None
		"""
		self.DIRTY_TILES_DISTANCES.append(math.sqrt(self.x_powers() + self.y_powers()))

		"""
			The Current Dirty Tile, Becomes The Last Dirty Tile
		"""
		self.L_POS_X = self.N_POS_X
		self.L_POS_Y = self.N_POS_Y

	def y_powers(self) -> float:

		"""
		Calculate Power of Two Y-axis Values Using Their Difference
		:return: power difference of two Y-axis values
		"""
		return math.pow(self.N_POS_Y - self.L_POS_Y, 2)

	def x_powers(self) -> float:

		"""
		Calculate Power of Two X-axis Values Using Their Difference
		:return: power difference of two X-axis values
		"""
		return math.pow(self.N_POS_X - self.L_POS_X, 2)

	def is_dirty(self) -> bool:

		"""
		Check If Current Tile Is Clean or Not
		:return: True | False
		"""
		if self.get_position_val() is 1:
			return True
		else:
			return False

	def clean(self) -> str:

		"""
		Clean Dirty Tiles By Just Setting Dirty Tile Value To 0
		Increment Tiles Cleaned
		Call calculate_distance
		:return: None
		"""

		self.set_position_val(0)    # Cleaning sets the current tile/position value to Zero|0

		self.calculate_distance()   # Calculate distance between two dirty tiles

		self.ROOM_TILES_CLEANED += 1    # Increment Number Of Clean Tiles After Each Clean
		return  'Clean'

	def percepts(self, env: Environment) -> None:

		"""
		Start The Process Of Cleaning The Environment
		:param env: The Environment The Vacuum Be Cleaning
		:return: None
		"""

		self.ROOM_GRID = env.get_room()

		self.START_TIME = time.time()   # Start timer

		"""
			While The Vacuum Has Not Reached The End Of The Room, Keep Cleaning
		"""
		while self.at_end(env):

			self.show_pos("start")  # For Debugging

			self.action()

		self.END_TIME = time.time()     # End Timer

	def action(self) -> str:

		"""
		:return: Returns An Action Done By The Vacuum
		"""
		if self.is_dirty():  # Check For Dirtiness
			return self.clean()  # Clean The Tile
		else:
			return self.move_horizontal_and_vertical()  # Keep Moving

	def at_end(self, env: Environment) -> bool:

		"""
		Checks Whether The Vacuum Has Reached The End Of The Environment
		:param env: Environment The Vacuum Is In
		:return bool: True | Fasle
		"""
		return self.N_POS_X is not env.get_rows() and self.N_POS_Y is not env.get_cols()

	def move(self, env: Environment) -> None:

		"""
		:param env: The Environment the Vacuum Will be Working in
		:return: None
		"""

		self.ROOM_GRID = env.get_room()     # Set Room To This Class Level Var

		"""
			Since This Is An N*M Matrix, we implement a nested for loop
			to traverse trough all indexes.
			Also helps in having ordered pairs of coords (x, y)
		"""
		self.START_TIME = time.time()
		for y in range(0, env.get_cols()):

			"""
				Vertical Axis
			"""

			for x in range(0, env.get_rows()):

				"""
					Horizontal Axis
					Whatever Matrix You Get, Transform It On The X-Axis Plane...
					Logical Miscalculations From My Side -_-
					x, y -> represent ordered paired coords (x, y)
				"""
				self.N_POS_Y = y
				self.N_POS_X = x

				self.show_pos("move")   # To Delete, FOR DEBUGGING PURPOSES

				if self.is_dirty():     # Check For Dirtiness

					print("dirty")
					self.clean()    # Clean The Tile

				else:
					self.move_horizontal_and_vertical()

		self.END_TIME = time.time()

		"""
			Set A Cleaned Room As The New Room
		"""
		print(self.ROOM_GRID)   # Debugging
		env.set_room(self.ROOM_GRID)    # Debugging

