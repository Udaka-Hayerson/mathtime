

class SpaceObjects:

    def __init__(self, name = '', weight = 0, gravity = 0.1, rotation_axis = 0.1, revolves_around = '',
                 speed_rotation_axis = 0, speed_revolves_around = 0):
        self.name = name
        self.weight = weight
        self.gravity = gravity
        self.rotation_axis = rotation_axis
        self.revolves_around = revolves_around
        self.speed_rotation_axis = speed_rotation_axis
        self.speed_revolves_around = speed_revolves_around

    def rotation_around_its_axis(self):
        return f'The {self.name} rotates on its axis at a speed {self.speed_rotation_axis}  kilometers per hour'

    def obj_revolves_around_obj(self):
        return f'{self.name} revolves around the {self.revolves_around} and develops a speed of ' \
               f'{self.speed_revolves_around} kilometers per hour in its orbit.'

    def gravity_in_obj(self):
        return f'The force of gravity on {self.name} is {self.gravity} g'

    def mass_of_the_obj(self):
        return f'The mass of the {self.name} is {self.weight} tons'

    def rotation_axis_obj(self):
        return f'At the {self.name}, The angle of inclination of the axis of rotation is {self.rotation_axis} degrees'

class Star(SpaceObjects):    #  derived class/child class

    def __init__(self, name, weight, gravity, rotation_axis, revolves_around, speed_rotation_axis,
                 speed_revolves_around, glow = '', constellation = ''):
        SpaceObjects.__init__(self, name, weight, gravity, rotation_axis, revolves_around,
                              speed_rotation_axis, speed_revolves_around)
        self.glow = glow
        self.constellation = constellation

    def star_glow(self):
        return f'The {self.name} shines with a power of {self.glow} candelas'

    def star_constellation(self):
        return f'The {self.name} star is located in the constellation {self.constellation}'


class Planet(SpaceObjects):

    def __init__(self, name, weight, gravity, rotation_axis, revolves_around, speed_rotation_axis,
                 speed_revolves_around,  atmosphere = False):
        SpaceObjects.__init__(self, name, weight, gravity, rotation_axis, revolves_around,
                              speed_rotation_axis, speed_revolves_around)
        self.atmosphere = atmosphere

    def i_have_atmosphere(self):
        if self.atmosphere:
            return f'Planet {self.name} has an atmosphere'
        else:
            return f' Planet {self.name} has no atmosphere'


class Satellites(SpaceObjects):
    def __init__(self, name, weight, gravity, rotation_axis, revolves_around, speed_rotation_axis,
                 speed_revolves_around, artificial = False):
        SpaceObjects.__init__(self, name, weight, gravity, rotation_axis, revolves_around,
                              speed_rotation_axis, speed_revolves_around)
        self.artificial = artificial

    def yes_no_artificial_obj(self):
        if not self.artificial:
            return f'The {self.name} is a natural satellite of the {self.revolves_around}'
        else:
            return f'The {self.name} is a artificial satellite of the {self.revolves_around}'


sun = Star('Sun', 5000000, 28.02, 7.25, 'a black hole', 3000, 27000000, '(2.84*10)**27', 'in different')
earth = Planet('Earth', 12000, 1.0, 23.26, sun.name, 1670, 107000, True)
moon = Satellites('Moon', 1350, 0.1654, 1.54, earth.name, 50, 3672, False)

print(sun.rotation_around_its_axis())
print(earth.rotation_around_its_axis())
print(moon.rotation_around_its_axis())

print(sun.obj_revolves_around_obj())
print(earth.obj_revolves_around_obj())
print(moon.obj_revolves_around_obj())

print(sun.gravity_in_obj())
print(earth.gravity_in_obj())
print(moon.gravity_in_obj())

print(sun.mass_of_the_obj())
print(earth.mass_of_the_obj())
print(moon.mass_of_the_obj())

print(sun.rotation_axis_obj())
print(earth.rotation_axis_obj())
print(moon.rotation_axis_obj())

print(sun.star_glow())
print(sun.star_constellation())

print(earth.i_have_atmosphere())

print(moon.yes_no_artificial_obj())
