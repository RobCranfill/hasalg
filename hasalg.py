''' hide and seek algorithm? 

    version 2, using turtle as "me"
'''
import math
import random
import time
import turtle


def random_loc():
    ''' return (x,y) each somewhere 0-150'''
    return random.random()*300 - 150, random.random()*300 - 150


def close_enough_to_target():
    dist = math.sqrt(turtle.xcor()*turtle.xcor() + turtle.ycor()*turtle.ycor())
    close_enough = (dist < 2)
    # print(f"  close_enough_to_target: {close_enough}")
    return close_enough


def pick_random_direction():
    dir = random.random() * 360
    print(f"pick_random_direction: {dir:0.0f}")
    return dir


def step_in_direction_is_warmer():
    ''' move in current dir; return "is that warmer?" '''

    old_dist = math.sqrt(turtle.xcor()*turtle.xcor() + turtle.ycor()*turtle.ycor())
    turtle.forward(1)
    new_dist = math.sqrt(turtle.xcor()*turtle.xcor() + turtle.ycor()*turtle.ycor())

    isWarmer = (old_dist > new_dist)
    print(f"  old dist {old_dist:0.2f}; new dist {new_dist:0.2f}; warmer? {isWarmer}")
    return isWarmer


def init_turtle():

    turtle.setworldcoordinates(-150, -150, 150, 150)
    turtle.title("Walkie-Talkie Hide-and-Seek Simulator")

    turtle.setpos(-1, 0)
    turtle.color("red")
    turtle.circle(2)

    turtle.penup()
    loc = random_loc()
    turtle.setpos(loc[0], loc[1])
    turtle.color("blue")
    turtle.pendown()


def hide_and_seek():

    init_turtle()

    stepNumber = 0
    while True:
        time.sleep(1)
        turtle.setheading(pick_random_direction())
        isWarmer = step_in_direction_is_warmer()
        while isWarmer:
            stepNumber += 1
            isWarmer = step_in_direction_is_warmer()
            print(f" Step # {stepNumber} to {turtle.xcor()}, {turtle.ycor()}")
            time.sleep(.02)
            if close_enough_to_target():
                print(f"\nGOTCHA! in {stepNumber} steps.")
                return # done!

        # # draw the tangent circle
        # turtle.penup()
        # turtle.setpos(0, )
        # turtle.color("green")
        # turtle.pendown()


hide_and_seek()

print("Press ctrl-C to exit")
turtle.mainloop()
