import turtle
import time
import random

# Set up the screen dimensions
WIDTH, HEIGHT = 700, 600
# Define a list of colors for the turtles
COLORS = ['red', 'green', 'blue', 'orange', 'yellow',
          'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racers():
    """
    Get the number of racers from the user input.
    The number must be between 2 and 10.
    """
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try again!')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Invalid number... Try again!')


def init_turtle():
    """
    Initialize the turtle screen with the specified width and height.
    """
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')


def create_turtles(colors):
    """
    Create turtle objects based on the provided colors.
    Position them evenly across the screen.
    """
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # Set the initial position of the turtles
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors):
    """
    Simulate the race by moving each turtle forward by a random distance.
    The first turtle to reach or exceed the top of the screen wins.
    """
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            # Check if the turtle has reached the top of the screen
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


# Get the number of racers from the user
racers = get_number_of_racers()
# Initialize the turtle screen
init_turtle()
# Shuffle and select colors for the turtles
random.shuffle(COLORS)
colors = COLORS[:racers]
# Start the race and determine the winner
winner = race(colors)
# Display the winner of the race
print('The', winner, 'turtle is the winner...')
# Pause for 5 seconds before closing the window
time.sleep(5)
