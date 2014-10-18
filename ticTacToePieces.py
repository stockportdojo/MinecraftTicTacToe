
# Work out who won
world.postToChat("Game Over")
if gameWon:
    if currentPlayer == NOUGHTS_BLOCK:
        world.postToChat("Noughts (Diamond) won!")
    else:
        world.postToChat("Crosses (Gold) won!")
else:
    world.postToChat("It's a draw!")


def getPlaySquare(playSquare):
    return world.getBlock(playSquare.x, playSquare.y, playSquare.z)


# Check the game grid to see if anyone won
# There's probably a neater way to do this
def checkIfPlayerWon(player):
    #Read all grid items
    playerBlockType = player.id
    currentSquareTopLeft = world.getBlock(playSquareTopLeft)
    currentSquareTopMiddle = world.getBlock(playSquareTopMiddle)
    currentSquareTopRight = world.getBlock(playSquareTopRight)
    if currentSquareTopLeft == playerBlockType and currentSquareTopMiddle == playerBlockType and currentSquareTopRight == playerBlockType:
        return True
    currentSquareMiddleLeft = world.getBlock(playSquareMiddleLeft)
    currentSquareMiddleMiddle = world.getBlock(playSquareMiddleMiddle)
    currentSquareMiddleRight = world.getBlock(playSquareMiddleRight)
    if currentSquareMiddleLeft == playerBlockType and currentSquareMiddleMiddle == playerBlockType and currentSquareMiddleRight == playerBlockType:
        return True
    currentSquareBottomLeft = world.getBlock(playSquareBottomLeft)
    currentSquareBottomMiddle = world.getBlock(playSquareBottomMiddle)
    currentSquareBottomRight = world.getBlock(playSquareBottomRight)
    if currentSquareBottomLeft == playerBlockType and currentSquareBottomMiddle == playerBlockType and currentSquareBottomRight == playerBlockType:
        return True
    if currentSquareBottomLeft == playerBlockType and currentSquareMiddleLeft == playerBlockType and currentSquareTopLeft == playerBlockType:
        return True
    if currentSquareBottomMiddle == playerBlockType and currentSquareMiddleMiddle == playerBlockType and currentSquareTopMiddle == playerBlockType:
        return True
    if currentSquareBottomRight == playerBlockType and currentSquareMiddleRight == playerBlockType and currentSquareTopRight == playerBlockType:
        return True
    return False



# Check if any blocks have been hit by a sword
blockHits = world.events.pollBlockHits()

# Check if any of the blocks that have been hit are empty spaces, and if they are, change them into
# the right kind of block for the current player
for blockHit in blockHits:
    blockHitType = world.getBlock(blockHit.pos)
    if blockHitType == EMPTY_BLOCK.id:
        world.setBlock(blockHit.pos, currentPlayer.id)


