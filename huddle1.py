#huddle1


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_()


for jump in range(6):
    step()

huddle
2


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def step():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        step()

    else:
        move()

huddle
4


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def step():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        step()
    else:
        move()