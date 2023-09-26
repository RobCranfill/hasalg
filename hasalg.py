''' hide and seek algorithm? '''
import math
import random
import time
import turtle


class State:
    ''' Now that we are using turtle graphics, we could get rid of this! '''
    def __init__(self, xy, dir):
        self.x = xy[0]
        self.y = xy[1]
        self.dir = dir

    def __repr__(self):
        return "State()"

    def __str__(self):
        return f"({self.x:0.0f},{self.y:0.0f}) - {self.dir:0.0f})"

def random_loc():
    ''' return (x,y) between 150 and 200, each'''
    return random.random()*50 + 150, random.random()*50 + 150

def close_enough_to_target(state):
    dist = math.sqrt(state.x*state.x + state.y*state.y)
    close_enough = (dist < 2)
    # print(f"  close_enough_to_target: {close_enough}")
    return close_enough

def pick_random_direction():
    dir = random.random() * 360
    print(f"pick_random_direction: {dir:0.0f}")
    return dir


def step_in_direction_is_warmer(myState):
    ''' move in current dir; return new state and "is that warmer?" '''

    old_dist = math.sqrt(myState.x*myState.x + myState.y*myState.y)

    x_inc = math.sin(math.radians(myState.dir))
    myState.x += x_inc
    y_inc = math.cos(math.radians(myState.dir))
    myState.y += y_inc

    new_dist = math.sqrt(myState.x*myState.x + myState.y*myState.y)

    isWarmer = (old_dist > new_dist)

    print(f"  old dist {old_dist:0.2f}; new dist {new_dist:0.2f}")
    print(f"  step_in_direction_is_warmer: {x_inc:0.2f},{y_inc:0.2f} -> {myState.x:0.0f}, {myState.y:0.0f}, {isWarmer}")
    return myState, isWarmer


def init_turtle(x, y):

    turtle.setworldcoordinates(-150, -150, 150, 150)
    turtle.title("Walkie-Talkie Hide-and-Seek Simulator")

    turtle.setpos(-1, 0)
    turtle.color("red")
    turtle.circle(2)

    turtle.penup()
    turtle.setpos(x, y)
    turtle.color("blue")
    turtle.pendown()


def hide_and_seek():

    seek_loc = (0,0) # the center of the screen
    my_state = State(random_loc(), 0) # should be random dir?
    print(f"Seek: {seek_loc} from {my_state}")

    init_turtle(my_state.x, my_state.y)

    step = 0
    while True:
        time.sleep(1)
        my_state.dir = pick_random_direction()
        turtle.setheading(my_state.dir)
        my_state, isWarmer = step_in_direction_is_warmer(my_state)

        turtle.setpos(my_state.x, my_state.y)

        while isWarmer:
            step += 1
            my_state, isWarmer = step_in_direction_is_warmer(my_state)

            turtle.setpos(my_state.x, my_state.y)
            # turtle.forward(1)

            print(f" Step # {step} to {my_state}")
            time.sleep(.1)
            if close_enough_to_target(my_state):
                print(f"\nGOTCHA! in {step} steps.")
                return # done!

hide_and_seek()

print("Press ctrl-C to exit")
turtle.mainloop()