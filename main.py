

class SpaceObjects:   #  base class/parent class

    def __init__(self, name = '', weight = 0, gravity = 0, revolves_around = '', speed_rotation_axis = 0, speed_revolves_around = 0):
        self.name = name
        self.weight = weight
        self.gravity = gravity
        self.revolves_around = revolves_around
        self.speed_rotation_axis = speed_rotation_axis
        self.speed_revolves_around = speed_revolves_around

    def rotation_around_its_axis(self):
        return self

    def obj_revolves_arount_obj(self, name, revolves_around):
        return f'{name} revolves around the {revolves_around} and is in its orbit.'

    @staticmethod
    def get_info():
        print('I am static method and I lie here and do nothing')

class Star(SpaceObjects):    #  derived class/child class
    @classmethod
    def classmethod(cls):
        print('Class method called')

    constellation = ''  #созвездие
    glow = 0

class Planet(SpaceObjects):

    solar_system = ''
    atmosphere = False
    orbit = ''

class Satellites(SpaceObjects):
    pass


#     artificial = False  # искусственный
#     non-circular orbit

# class Comet(SpaceObjects):
#
#     speed = 0
#     lenght_tail = 0
#
# class Asteroids(SpaceObjects):
#
#     speed = 0
#
# class Spaceships(SpaceObjects):
#     yearofthelaunch = 0