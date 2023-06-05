#Simulate the DVD "paused" screen (inspired by the 2023 SKHS music trip)

#-----INITIALIZATION-----

#Import modules
import turtle as trtl
import random as rand
import time

#Initialize variables
x_speed = 6
y_speed = 1

#Initialize screen
wn = trtl.Screen()
wn.setup(900, 600)
wn.bgcolor("black")

#Set up the logo
logo = trtl.Turtle()
logo.penup()

#different icons
red = "red.gif"
wn.register_shape(red)
green = "green.gif"
wn.register_shape(green)
blue = "blue.gif"
wn.register_shape(blue)

logo.shape(red)


def bounce(direction):
    global x_speed, y_speed
    if direction == 'x':
        x_speed = (-1 * x_speed)
    if direction == 'y':
        y_speed = (-1 * y_speed)

def bounce2():
    '''Theoretically, this should make the logo bounce at a right angle (more like the actual pause screen),
    but for some reason it's just sending the logo back the way it came.
    Thus, this function is a work in progress.'''
    global x_speed, y_speed
    #bounce at a right angle = perpendicular slopes = opposite reciprical
    #current slope: y/x
    #new slope: -x/y --> formula needs to be y = -x, x = y
    tempx = x_speed
    tempy = y_speed

    x_speed = tempy
    y_speed = -1 * tempx

def changeColor(logo):
    logo.shape(rand.choice([red, blue, green]))
    wn.update()

while True:
    #Add a slight delay to the program -- this loop will (theoretically) run 100 times per second
    time.sleep(0.01)

    logo.goto(logo.xcor() + x_speed, logo.ycor() + y_speed)

    #logo is 200x100 pixels
    if logo.xcor() < (-450 + 100) or logo.xcor() > (450 - 100):
        bounce('x')
        changeColor(logo)
    if  logo.ycor() < (-300 + 50) or logo.ycor() > (300 - 50):
        bounce('y')
        changeColor(logo)

    #Update screen
    wn.update()

wn.listen()
trtl.mainloop()