import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Game")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def turtle_right():
    turtle_instance.right(10)

def turtle_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()



drawing_board.listen()
drawing_board.onkey(turtle_forward,"space")
drawing_board.onkey(turtle_right,"Down")
drawing_board.onkey(turtle_left,"Up")
drawing_board.onkey(clear_screen,"Escape")
drawing_board.onkey(return_home,"q")
turtle.mainloop()