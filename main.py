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
guess_state = []

while len(guess_state)<50:
    answer_state = screen.textinput(title=f"Guess the States{len(guess_state)}/50", prompt="What's another State").title()
    if answer_state == "Exit":
        miss_state = [state for state in state_list if state not in guess_state]
        new_data = pd.DataFrame(miss_state)
        new_data.to_csv("learn_data.csv")
        break
    if answer_state in state_list:
        guess_state.append(answer_state)
        location=state_list.index(answer_state)
        x_cor=x_cor_list[location]
        y_cor=y_cor_list[location]
        bekos.goto(x_cor, y_cor)
        bekos.write(answer_state, move=False, align="center", font=FONT)

