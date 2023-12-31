import turtle
import time

def draw_letter_A():
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(120)
    turtle.forward(50)

def draw_letter_k():
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(50)
    turtle.right(45)
    turtle.forward(70)
    turtle.backward(70)

def draw_letter_n():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(70)
    turtle.left(135)
    turtle.forward(50)

def draw_letter_s():
    turtle.circle(25, -180)
    turtle.right(180)
    turtle.circle(25, -180)

def draw_name_animation():
    turtle.speed(2)

    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()

    # Draw letter 'A'
    draw_letter_A()
    turtle.penup()
    turtle.goto(-120, 0)
    turtle.pendown()

    # Draw letter 'k'
    draw_letter_k()
    turtle.penup()
    turtle.goto(-90, 0)
    turtle.pendown()

    # Draw letter 'a'
    draw_letter_A()
    turtle.penup()
    turtle.goto(-60, 0)
    turtle.pendown()

    # Draw letter 'n'
    draw_letter_n()
    turtle.penup()
    turtle.goto(-30, 0)
    turtle.pendown()

    # Draw letter 's'
    draw_letter_s()

    time.sleep(2)
    # turtle.clear()

if __name__ == "__main__":
    draw_name_animation()
    turtle.done()
