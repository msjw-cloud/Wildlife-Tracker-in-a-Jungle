class Jungle_Environment:
    def __init__(self, N, ambulance, F_orientation, Trees_location, Shed_init_locaiton, Shed_status, Needle_num):
        self.N = N
        self.ambulance = ambulance
        self.Trees_location = Trees_location
        self.Shed_init_location = Shed_init_locaiton
        self.Shed_status = Shed_status
        self.Needle_num = Needle_num
        self.F_orientation = F_orientation
        self.state = (self.ambulance, self.F_orientation, self.Needle_num, False, 2, self.Shed_init_location)