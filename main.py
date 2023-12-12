import random
import turtle

screen = turtle.Screen()
screen.bgcolor("light green")
game_over = False
score = 0
FONT = ('Veranda', 30, 'normal')

#turtle list
turtle_list = []

#countdown turtle
count_down_turtle = turtle.Turtle()

# score turtle
score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark green")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    score_turtle.setposition(0, y)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)



def make_turtle(x, y):
    t = turtle.Turtle()


    def handle_click(x, y):
        global score
        score +=1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)
        print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(1.5, 1.5)
    t.color("dark green")
    t.goto(x *10, y * 10)
    t.pendown()
    turtle_list.append(t)


def setup_turtles():
    for x in range(-40,40,10):
        for y in range(-40,40,10):
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 200)


def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 30)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write(f"Time: {time}",move=False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write("Game Over!", align='center', font=FONT)
        hide_turtles()

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()