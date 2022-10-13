ROTATIONVALUE = {
    'L': -1,
    'R': 1
}


def rotate(current_direction, rotation_direction):
    return (current_direction + ROTATIONVALUE[rotation_direction]) % 4
