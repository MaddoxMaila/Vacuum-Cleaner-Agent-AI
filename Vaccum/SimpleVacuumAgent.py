import random

class SimpleVacuumAgent:

	@staticmethod
	def vacuum(percepts: dict) -> str:

		if percepts.get("room") is 'A':
			return 'right'
		elif percepts.get("room") is 'B':
			return 'left'


DIRTY = 1
CLEAN = 0


def create_rooms() -> list:

	rooms = []

	for x in range(0, 2):

		random_num = random.uniform(0, 1)

		if random_num <= 0.10:
			rooms.append(DIRTY)
		else:
			rooms.append(CLEAN)

	return rooms


print(create_rooms())

