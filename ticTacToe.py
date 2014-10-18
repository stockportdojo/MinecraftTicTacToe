# Include the code we need
import mcpi.minecraft as minecraft
import mcpi.block as block
from vec3 import Vec3

# Set up some variables so we can refer to them more easily later
FENCE_BLOCK = block.FENCE
EMPTY_BLOCK = block.WOOL
AIR_BLOCK = block.AIR
STONE_BLOCK = block.STONE

NOUGHTS_BLOCK = block.DIAMOND_BLOCK
CROSSES_BLOCK = block.GOLD_BLOCK

# Set up the positions of the blocks in our game grid
leftColumn = 1
middleColumn = 3
rightColumn = 5

topRow = 6
middleRow = 4
bottomRow = 2

playSquareTopLeft = Vec3(leftColumn, topRow, 0)
playSquareTopMiddle = Vec3(middleColumn, topRow, 0)
playSquareTopRight = Vec3(rightColumn, topRow, 0)
playSquareMiddleLeft = Vec3(leftColumn, middleRow, 0)
playSquareMiddleMiddle = Vec3(middleColumn, middleRow, 0)
playSquareMiddleRight = Vec3(rightColumn, middleRow, 0)
playSquareBottomLeft = Vec3(leftColumn, bottomRow, 0)
playSquareBottomMiddle = Vec3(middleColumn, bottomRow, 0)
playSquareBottomRight = Vec3(rightColumn, bottomRow, 0)

# Connect to Minecraft
world = minecraft.Minecraft.create()

currentPlayer = NOUGHTS_BLOCK
gameWon = False
gameRunning = True
movesLeft = 9

# Clear space around our game area
world.setBlocks(-20,0,-20,20,20,20, AIR_BLOCK)
world.setBlocks(-10, -1, -5, 10, -1, 5, STONE_BLOCK)

# Build our play area
world.setBlock(0,0,0, FENCE_BLOCK)
world.setBlocks(0,1,0,6,7,0, FENCE_BLOCK)
world.setBlock(6,0,0, FENCE_BLOCK)

# Place our "Empty space" blocks
world.setBlock(playSquareTopLeft, EMPTY_BLOCK)
world.setBlock(playSquareTopMiddle, EMPTY_BLOCK)
world.setBlock(playSquareTopRight, EMPTY_BLOCK)
world.setBlock(playSquareMiddleLeft, EMPTY_BLOCK)
world.setBlock(playSquareMiddleMiddle, EMPTY_BLOCK)
world.setBlock(playSquareMiddleRight, EMPTY_BLOCK)
world.setBlock(playSquareBottomLeft, EMPTY_BLOCK)
world.setBlock(playSquareBottomMiddle, EMPTY_BLOCK)
world.setBlock(playSquareBottomRight, EMPTY_BLOCK)

# Teleport the play in front of the game grid
world.player.setTilePos(4,3,-3)

# Tell the player we're ready
world.postToChat("Let's play!")
world.postToChat("Noughts (Diamond) plays first")
