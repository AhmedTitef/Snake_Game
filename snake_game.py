import turtle
import time
import random

delay = 0.1

# set up screen


windowObject = turtle.Screen()
windowObject.title("Snake Game")
windowObject.bgcolor("green")
windowObject.setup(width=600, height=600)
windowObject.tracer(0)  # turns off animation (screen updates)

# create snake head
head = turtle.Turtle()
head.speed(0)  # animation speed of turtle module
head.shape("square")
head.color("black")
head.penup()  # pen up it wont make the snake draw a line where it goes. there is pendown
head.goto(0, 0)  # start in center of screen
head.direction = "stop"

# making food
food = turtle.Turtle()
food.speed(0)  # animation speed of turtle module
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)  # start in center of screen

# body segments
segments = []  # when the player touchees the food we add a segment


# functions

def go_up():
    if head.direction != "down": #this prevents going up then down or vice versa
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"



def go_right():
    if head.direction != "left":
        head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard binding it connects a keypress to a function
windowObject.listen()
windowObject.onkeypress(go_up, "w")  # keypress takees a function with no argument thats why there is no paratethees
windowObject.onkeypress(go_down, "s")
windowObject.onkeypress(go_left, "a")
windowObject.onkeypress(go_right, "d")

# main game loop
while True:
    windowObject.update()


    #check for a collison with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"


        # hide the elements
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segment list
        segments.clear()

    if head.distance(food) < 20:  # we choose 20 becasue the food circle by defualt is 20 pixels x 20 pixels
        # so if the it is less than 20 that means we went inside it (collision)
        # that means they colided and move the food to a randowm spot
        x = random.randint(-290,
                           290)  # the screen is from -300 to 300(starts from center and 300 left or 300 right) which is 600 pixels total
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # move the end segments first in reverse order
    # here works if there is more than one segment in the segments list
    for index in range(len(segments) - 1, 0, -1):  # decrements by 1 till 0
        x = segments[index - 1].xcor()

        y = segments[index - 1].ycor()

        segments[index].goto(x, y)

    # move segment 0 to where the head is

    if len(segments) > 0:  # it takes the coordinates of the head and give it to the first element of the array
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head collosion with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the elements
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segment list
            segments.clear()

    time.sleep(delay)

windowObject.mainloop()  # this will keep windows open
