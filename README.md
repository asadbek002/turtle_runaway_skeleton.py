# turtle_runaway_skeleton.py
RunawayGame Class:

Manages the game mechanics.
Controls the initialization of game elements, starting the game, checking if the runner is caught, and updating the game state.
Provides different difficulty levels: easy, medium, and hard.
Castle Class:

Represents a castle on the game screen.
Inherits from turtle.RawTurtle.
Drawn as a square with a gray color.
Bush Class:

Represents a bush on the game screen.
Inherits from turtle.RawTurtle.
Drawn as a circle with a green color.
ManualMover Class:

Represents a manual mover, allowing the player to control movement using arrow keys.
Inherits from turtle.RawTurtle.
Handles arrow key presses for forward, backward, left, and right movement.
RandomMover Class:

Represents a mover with random movements.
Inherits from turtle.RawTurtle.
Moves randomly in one of three directions: forward, left, or right.
Villain Class:

Represents a villain character in the game.
Inherits from turtle.RawTurtle.
Moves towards the player's position to catch them.

Creates a tkinter canvas and a turtle screen for the game.
Instantiates the game elements (runner, chaser, villain, castle, bushes) and sets their initial positions and behaviors.
Starts the game loop and handles the game's mechanics, including updating the game state and checking for a win or loss.
The game starts with the runner and the chaser positioned at a distance from each other. The objective of the game is for the runner to avoid being caught by the chaser and the villain while navigating the game area. The game includes features like different difficulty levels, visual elements (castle, bushes), and the possibility of adding a logo for an educational institution (Seoul National University in this case).

Players can control the runner's movements in manual mode or let the chaser and villain move automatically in different directions. The game provides feedback on whether the runner was caught or not.

<img src="https://github.com/asadbek002/Text_recognition/blob/main/result.png" width="500" height="300">
