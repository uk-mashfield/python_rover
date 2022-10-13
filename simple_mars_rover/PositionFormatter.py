COMPASS = ['N', 'W', 'S', 'E']


def format_position(direction, x, y) -> str:
    return f'{x}:{y}:{COMPASS[direction]}'
