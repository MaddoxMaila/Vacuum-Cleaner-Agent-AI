from Vaccum.Environment import Environment
from Vaccum.VacuumCleaner import VacuumCleaner


Room = Environment(1, 2)

Room.build_room()

VacuumAgent = VacuumCleaner(Room.get_rows(), Room.get_cols())

VacuumAgent.move(Room)
