from simple_mars_rover.MovementCalculator import move
from simple_mars_rover.RotationCalculator import rotate
from simple_mars_rover.PositionFormatter import format_position


class MarsRover:

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__direction = 0

    def execute(self, command):
        for cmd in command:
            if cmd == 'M':
                self.__x, self.__y = move(self.__direction, self.__x, self.__y)
            else:
                self.__direction = rotate(self.__direction, cmd)

        return format_position(self.__direction, self.__x, self.__y)
