# apollo-and-diana
The purpose of this project was to solve the "Apollo and Diana" maze problem. 

### Background
This problem is based on the “Apollo and Diana” maze problem (from “MAD MAZES: Intriguing Mind Twisters
for Puzzle Buffs, Game Nuts and Other Smart People” by Robert Abbott, Bob Adams, Inc. Publishers, 1990). The
text of the problem is quoted below. 

### Story
Apollo, god of the sun, stole a set of arrows from his sister Diana, goddess of the moon. When Diana
caught him shooting moonbeams instead of sunbeams, she was furious! She cast a mighty curse, and all
his arrows fell around him in a terrible maze. That maze is shown here. Apollo’s sunbeams are the red
arrows; Diana’s moonbeams are the blue arrows.
Diana spoke to Apollo: “You will remain here in this field of arrows until you solve this puzzle. You must
find a route from the red arrow at the upper left to the bull’s-eye at the lower right. The first red arrow
points to two blue arrows. Choose either of those blue arrows and move to it. You are now on a blue
arrow that points to one or more red arrows. Choose one of those red arrows. and move to it. Continue
in this fashion, alternating between red and blue arrows. If you are truly wise you will arrive at an arrow
that points to the bull’s eye. You may then proceed to the bull’s eye and escape from the maze. It’s far
more likely, though, that you will wander into a loop and find yourself going around endlessly. If that
happens, you can admit that you are lost, go back to the red arrow at the upper left, and start the puzzle
over again.”
So, how can Apollo find his way to the bull’s eye (without getting stuck in too many loops)?

### Input
The input file contains multiple instances. The input file begins with a single positive integer on a line by itself
indicating the number of instances following, each of them as described below. This line is followed by a blank
line, and there is also a blank line between consecutive instances.
Each instance begins with a single positive integer on a line by itself indicating the dimension, n, of the maze.
The following lines contain the directional and color information for each square of the maze. There are n lines
which each have n values. Each value is represented as a direction followed by a dash (i.e., -) followed by the
color. The direction is represented using N, S, E, W, NE, NW, SE, SW to represent “north”, “south”, “east”,
“west”, “northeast”, “northwest”, “southeast”, and “southwest”, respectively. The color is represented using
R, B to represent “red” and “blue”, respectively. 0 represents the goals square (bull-eye).

### Output
The output file should contain one line for each instance. There should be a blank line between consecutive
outputs.
The output for each instance should consist of a path from the top left square to the bottom right square
(bull-eye). There should be a single line of output which indicates the path Apollo should take. Each move
should be represented by a direction and an integer representing the number of squares moved. The direction
should be represented using N, S, E, W, NE, NW, SE, SW to represent “north”, “south”, “east”, “west”,
“northeast”, “northwest”, “southeast”, and “southwest”, respectively. There should be a dash between the
integer representing the number of squares moved and the direction. Each move should be separated by a
space

## Running
To compile the code for project three you only need a simple command
`“python project_3.py”`

For this project will assume that a file name input.txt will be in the same current working directory. The program will output a file called enzinna.txt in the same current directory.

## Date Completed
Spring 2014 - University of South Florida
