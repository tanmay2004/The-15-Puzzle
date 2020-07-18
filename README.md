# The-15-Puzzle
This is the 15 puzzle game I have created using the Pygame module with Python. The aim is to arrange the numbers in the correct order from 1 to 15 going row by row.

The initial board setup is chosen randomly by the program. This could produce unsolvable puzzles, which can be checked using an algorithm described in detail [here](https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html) and [here](https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/). So, the program checks if the board position is an impossible one and randomly generates new ones until a valid starting position is obtained.

When you win, the 16th tile is automatically added to the board in its rightful place. The screenshot below is an example of the finished board you would see!

![](https://raw.githubusercontent.com/tanmay2004/Graphic-Games-with-Pygame/master/winning15_ss.PNG)

You will have to manipulate the tiles on the board into reaching the correct positions by making use of the empty white square. You can move the tiles adjacent to this tile into that place using the below two methods:
* Clicking on the tile you wish to move
* Using the 4 arrow keys

**Note:** You can switch between these controls at any point while playing the game.
