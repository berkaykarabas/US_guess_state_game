import turtle
import pandas as pd
FONT = ("Times New Roman", 10, "normal")
screen = turtle.Screen()
screen.title("U.S. State Game")
score = 0
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
bekos = turtle.Turtle()
bekos.penup()
bekos.hideturtle()
data = pd.read_csv("50_states.csv")
state_list = data["state"].tolist()
x_cor_list = data["x"].tolist()
y_cor_list = data["y"].tolist()

is_on = True
while is_on:

    answer_state = screen.textinput(title=f"Guess the States{score}/50", prompt="What's another State")

    if answer_state in state_list:
        location=state_list.index(answer_state)
        x_cor=x_cor_list[location]
        y_cor=y_cor_list[location]
        bekos.goto(x_cor, y_cor)
        bekos.write(answer_state, move=False, align="center", font=FONT)
        score += 1
    else:
        bekos.goto(0,0)
        bekos.write(f"Game Over! there is not State in U.S. Your score is:{score}",move=False,align="center",font=FONT)
        is_on = False

turtle.mainloop()
