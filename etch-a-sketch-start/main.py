from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def reset_drawing():
    tim.reset()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.right(10)


def move_clockwise():
    tim.left(10)


screen.listen()
screen.onkey(move_forwards, "space")
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=reset_drawing)
screen.exitonclick()
