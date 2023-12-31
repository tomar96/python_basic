class Remote:
    pass
class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass
    def moveDown(self):
        pass
Remote1 = Remote()
Player1 = Player()
if(Remote1.isLeftPressed()):
    Player1.moveLeft()