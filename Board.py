import Scores
class Board(Scores.Scores):
    def __init__(self):
        self.board = []
        for i in xrange(0,8):
            self.board.append([])
            for j in xrange(0,8):
                self.board[i].append(Square())
        wPairs = [(1,2),(2,2),(3,2),(4,2)]
        for i in wPairs:
            self.setWSquare(i[0],i[0],i[1])
        pairs = [(0,3,2),(2,6,2),(3,7,2),(6,6,2),(1,5,3),(5,5,3)]
        for i in pairs:
            self.setLSquare(i[0],i[1],i[2])
            self.setLSquare(i[1],i[0],i[2])
        for i in [0,7]:
            for j in [0,7]:
                self.setWSquare(i,j,3)
        self.setWSquare(7,7,None)
        
        rotated = zip(*self.board[::-1])
        out = []
        for i in zip(self.board,rotated):
            out.append(i[0]+ list(i[1][1:]))
        for i in out[6::-1]:
            out.append(i)
        self.board = out
    def __repr__(self):
        out = ""
        for i in self.board:
            out = out+str(i)+"\n"
        return out      

    def setLSquare(self,x,y,val):
        self.board[x][y] = Square(letterModifier = val)
    def setWSquare(self,x,y,val):
        self.board[x][y] = Square(wordModifier = val)

class Square:
    """
        modifiers should be functions that return an int
        to which a letter or word score can be multiplied
        by
    """
    def __init__(self,letterModifier=None,wordModifier=None):
        self.letterModifier = letterModifier
        self.wordModifier   = wordModifier
        self.tile = None
    def setTile(self,tile):
        # Modifiers cannot be used once a tile has been placed
        self.letterModifier = None
        self.wordModifier = None
        self.tile = tile
    def getTile(self):
        return self.tile
    def __or__(self,other):
        return (self.letterModifier or self.wordModifier) or (other.letterModifier or other.wordModifier) 
    def __repr__(self):
        if self.tile != None:
            return str(self.tile.label)+' '
        elif self.wordModifier != None:
            return str(self.wordModifier)+'w'
        elif self.letterModifier != None:
            return str(self.letterModifier)+'l'
        return str('  ')
                
    def __str__(self):
        return self.modifier
if __name__ == "__main__":
    t = Board()
    print t
