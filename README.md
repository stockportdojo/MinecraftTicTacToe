MinecraftTicTacToe
==================

Oh noes! I was happily hacking away making a Tic Tac Toe game in Minecraft, when a creeper blew up my house and ruined my laptop!

Here are the pieces of code I managed to save. Can you turn them into a working Tic Tac Toe game?

###How the game should work:###

When the script is started, it builds a Tic Tac Toe game board, and teleports the player next to it. Players take turns using the
mouse and keyboard to make their move.

The player then hits a wool block with their sword to choose their block. First player to play is Noughts, and each block they hit becomes a Diamond block.
Crosses plays next, and the block they hit with the sword becomes a Gold block.

When one player has 3 blocks in a row (up and down or side to side), they win the game. If all blocks have been hit then the game is a draw.

The script should let the players know who is playing next, and should tell tem in chat if they have won, or if the game is over.

When the game has finished, the script can stop.

## Getting Started ##

First start up your Raspberry Pi and make a folder to store your Tic Tac Toe game code:

```bash
mkdir ~/tictactoe
cd ~/tictactoe
```

I've stored all the pieces of code I could find on Github. You can clone the code directly from Github using the command:

```bash
git clone git@github.com:stockportdojo/MinecraftTicTacToe.git .

```

**Important:** The dot (.) at the end matters!

The working code is all in ```ticTacToe.py```. Some other snippets of incomplete helpful (or unhelpful) code are in ```ticTacToePieces.py```.

Make sure you have Minecraft running, create a new world if you need to, then start IDLE.

Once IDLE is open, use the File menu to open ```ticTacToe.py```.

Have a look at the code. You can see I've put code comments in to make it easier to find your way around the code that
is already in place.

If you run the code now (Press F5 in IDLE), it makes the game board, teleports the player, and announces in chat that it is
ready to play. Unfortunately, that's as far as I got. The ```ticTacToePieces.py``` file has some code snippets that were part of
my original game, or that I found while picking up the burnt pieces of my laptop. Some of them will tell you what they are for, 
others won't be so obvious so you'll have to work out what they do. Some pieces might not do anything useful at all.

Good luck - and keep on saving your work so the creepers don't blow up yours too!

## Extra challenges ##

Once you've got the basic game working, you might like to make some of the changes that I had planned before the explosion:

1. Allow players to win if they get 3 blocks in a row diagonally
2. Make sure players can't cheat by replacing blocks
3. Have the game reset so it can be played again over and over, without restarting the script
4. One player mode - have the Gold player controlled by the script - this one is complicated! You need to come up with a way of 
working out the next sensible move to make - just picking free spots at random won't be much of a challenge to a player!
5. ***Super Challenge*** Find another way to choose the players moves - like pressing a button connected to the GPIO pins on your Pi, or playing by Twitter.
