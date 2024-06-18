from turtle import Turtle, Screen

turt = Turtle()
turt.color("blue")
screen = Screen()

turt.speed(0)  

initial_size = 20
increment = 10
number_of_squares = 50
turt.penup()
turt.goto(100, -100)
turt.pendown()

turt.setheading(0)

for i in range(initial_size, initial_size + number_of_squares * increment, increment):
    
    for _ in range(4):
        turt.forward(i)
        turt.left(90)

    turt.penup()
    turt.backward(increment)
    turt.right(90)
    turt.forward(increment)
    turt.setheading(0)
    turt.pendown()

screen.mainloop()
