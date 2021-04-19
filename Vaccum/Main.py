from Vaccum.Environment import Environment
from Vaccum.VacuumCleaner import VacuumCleaner

"""
	Vacuum Cleaner Agent
	Dirty Rooms = 1
	Clean Rooms = 0
	
	Environment Class Builds The Rooms Randomly With 10% Chance Of The Room Being Dirty!
	Vacuum Will Traverse Each Room Sequentially, 
	If The Room Is Dirty -> Cleans The Room
	If The Room Is Clean -> Keeps Moving
	Each Movement( Cleaning/ Moving) Will Cost The Vacuum 1sec Of Time
"""


def seed_env(n: int, m: int) -> None:

	print("\n\n*** A Randomly Created Dirty/Clean {}*{} Environment ***".format(n, m))

	room = Environment(n, m)    # Creates Room of n-rows & m - columns

	room.build_room()   # Builds The Room With Randomly Selected Dirty Squares

	vacuum_agent = VacuumCleaner(room.get_rows(), room.get_cols())  # Creates The Vacuum Agent

	vacuum_agent.percepts(room)     # Feeds The Agent Perception Of The Room

	print("Number Of Tiles Cleaned : {}".format(vacuum_agent.get_tiles_cleaned()))

	distances = vacuum_agent.get_dirty_distances()

	if len(distances) > 0:

		print("\n*********Distance Traveled To The Next Dirty Room********\n")
		for distance in distances:

			print("A={}\nB={}\nDistance={}\n".format(distance.get("A"), distance.get("B"), distance.get("distance")))
	else:
		print("*** No Tiles Cleaned -> No Distance Calculated Between Dirty Tiles")

	print("\n***** TIME METRICS *****")
	start_time = float(vacuum_agent.get_time().get("start"))
	end_time = float(vacuum_agent.get_time().get("end"))
	time_diff = end_time - start_time
	# print("Start Time : {}".format(vacuum_agent.get_time().get("start")))
	# print("End Time   : {}".format(vacuum_agent.get_time().get("end")))
	print("Time Taken : {} seconds".format(time_diff))
	print("\n************************************************************************")


# seed_env(100, 100)

seed_env(1, 2)  # Demonstrates The Example From The Slides

# Increases The Number Of Rooms To Clean

seed_env(3, 3)

seed_env(3, 5)

# Your Own Environment!...
