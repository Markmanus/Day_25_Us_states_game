import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
wrong_guesses = 3
correct_guesses = 0

turtle.shape(image)
df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
number_of_states = len(all_states)
guessed_states = []


while len(guessed_states) < 50 and wrong_guesses > 0:

    answer_state = screen.textinput(title=f"Guess the State ",

                                prompt=f"What's another state's name?{correct_guesses}/{number_of_states}" ).title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        correct_guesses += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    elif wrong_guesses == 0:
        screen.textinput(title="Game Over", prompt="You lose. Press enter to exit.")
        screen.exitonclick()

    else:
        wrong_guesses -= 1
        print(f"Wrong guess. You have {wrong_guesses} guesses left.")

states_to_learn = [state for state in all_states if state not in guessed_states]
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")



