from Vaccum.Environment import Environment
from Vaccum.VacuumCleaner import VacuumCleaner


Room = Environment(10, 10)

Room.build_room()

VacuumAgent = VacuumCleaner(Room.get_rows(), Room.get_cols())

VacuumAgent.move(Room)

print(Room.get_room())
print(VacuumAgent.get_tiles_cleaned())
print(VacuumAgent.get_dirty_distances())
print(VacuumAgent.get_time().get("start"))
print(VacuumAgent.get_time().get("end"))
