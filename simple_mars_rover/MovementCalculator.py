def __move_north(x, y):
    y = (y + 1) % 10
    return x, y


def __move_south(x, y):
    y = (y - 1) % 10
    return x, y


def __move_west(x, y):
    x = (x + 1) % 10
    return x, y


def __move_east(x, y):
    x = (x - 1) % 10
    return x, y


def move(direction, x, y):
    movement = [
        __move_north,
        __move_west,
        __move_south,
        __move_east,
    ]
    func = movement[direction]  # get movement from strategy
    return func(x, y)
