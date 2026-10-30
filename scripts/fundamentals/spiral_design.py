# PROGRAM: Spiral Design
# PURPOSE: Create a spiral design using Turtle Graphics.
# INPUT: Number of spiral turns and distance between each turn from the user.
# PROCESS: Draw a spiral pattern with varying colors.
# OUTPUT: A colorful spiral design displayed on the screen.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

import turtle
import random

def draw_spiral(turtle_obj, turns, distance):
    """Draw a spiral pattern with specified turns and distance."""
    for i in range(turns):
        color = (random.random(), random.random(), random.random())  # Generate a random color
        turtle_obj.color(color)
        turtle_obj.forward(distance)
        turtle_obj.right(45)  # Change the angle to create a spiral effect
        distance += 5  # Increase distance for the next line

def main():
    """Main function to create a spiral design."""
    screen = turtle.Screen()
    screen.bgcolor("white")

    user_turns = int(turtle.numinput("Input", "Enter the number of spiral turns: ", minval=1, maxval=100))
    distance_between_turns = int(turtle.numinput("Input", "Enter the distance between each turn: ", minval=10, maxval=200))

    # Create a turtle object
    spiral_turtle = turtle.Turtle()
    
    draw_spiral(spiral_turtle, user_turns, distance_between_turns)

    turtle.done()

if __name__ == "__main__":
    main()
