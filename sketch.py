from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(2)
    
def move_backwards():
    tim.backward(2)

def counter_clockwise():
    tim.left(5)
    
def clockwise():
    tim.right(5)
    
def clear_drawing():
    tim.reset()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_drawing, "c")
screen.exitonclick