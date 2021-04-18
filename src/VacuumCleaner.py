

class Vacuum :

	ROOM_GRID = None
	ROOM_ROWS = 0
	ROOM_COLS = 0

	N_POS_X = 0
	N_POS_Y = 0
	L_POS_X = 0
	L_POS_Y = 0

	def __init__(self, grid_rows, grid_cols):

		self.ROOM_COLS = grid_cols
		self.ROOM_ROWS = grid_rows

	def move_horizontal_and_vertical(self):

		if self.N_POS_X >= 0:  # Will Change The Vacuum Direction To Move From Left To Right

			if self.N_POS_X is 0:
				self.down()     # Move The Vacuum Down

			self.N_POS_X += 1   # This Imitates Moving To The Right

		elif self.N_POS_X <= self.ROOM_ROWS:    # Will Change The Vacuum Direction To Move From Right To Left

			if self.N_POS_X is self.ROOM_ROWS:
				self.down()

			self.N_POS_X -= 1   # This Imitate Moving To The Left

	def up(self):

		if self.N_POS_Y is not 0 or self.N_POS_Y is not self.ROOM_COLS:
			self.N_POS_Y -= 1

	def down(self):

		if self.N_POS_Y is not 0 or self.N_POS_Y is not self.ROOM_COLS:
			self.N_POS_Y += 1

	def set_position_val(self, val):
		self.ROOM_GRID[self.N_POS_X][self.N_POS_Y] = val

	def get_position_val(self):
		return self.ROOM_GRID[self.N_POS_X][self.N_POS_Y]

	def is_dirty(self):

		if self.get_position_val() is 0:
			return True
		else:
			return False

	def clean(self):

		self.set_position_val(0) # Cleaning sets the current tile/position value to Zero|0

	def move(self, env):

		if self.is_dirty():
			self.clean()
		else:

			self.move_horizontal_and_vertical()