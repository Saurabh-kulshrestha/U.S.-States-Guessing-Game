import turtle
import pandas

# Read the CSV file containing state names and coordinates
data = pandas.read_csv("50_states.csv")

# Remove any extra whitespace from the state names
data["state"] = data["state"].str.strip()

# Convert the state column into a list for easy lookup
state_list = data["state"].to_list()

# Create a turtle object to write state names on the map
marker = turtle.Turtle()
marker.hideturtle()  # Hide the turtle icon
marker.penup()       # Prevent turtle from drawing lines

# Set up the screen for the game
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load and set the background image of the U.S. map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Keep track of correctly guessed states
guessed_states = []

# Game loop: continues until 50 states are guessed
while len(guessed_states) < 50:
    # Ask the user to input the name of a state
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()  # Capitalize the input to match CSV formatting

    # If the user types 'Exit', save the missing states to a file and quit
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If the answer is valid and not already guessed
    if answer_state in state_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Get the coordinates of the guessed state from the CSV
        coordinates = data[data["state"] == answer_state]
        x_cord = coordinates["x"].values[0]
        y_cord = coordinates["y"].values[0]

        # Move the turtle to the coordinates and write the state name
        marker.goto(x_cord, y_cord)
        marker.write(answer_state, align="center", font=("Arial", 8, "bold"))
