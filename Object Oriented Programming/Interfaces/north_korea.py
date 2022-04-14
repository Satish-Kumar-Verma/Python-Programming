

class nuclear_missile(object):
    def __init__(self):
        self.__target = "None"
        self.__coordinate = "None"
        self.__mode = "On the hit"

    def set_target(self, target):
        self.target = target

    def get_target(self):
        return self.target

    def set_coordinate(self, coordinate):
        self.coordinate = coordinate

    def set_mode(self, mode):
        self.mode = mode

    def initialize(self):
        print(f"Sending a nuclear missile to {self.target}, Coordinate : {self.coordinate}")
