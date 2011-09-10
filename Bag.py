import random
import Scores
class Bag:
    ## A big ol' bag of tiles
    def __init__(self):
        self.tiles = []
        tileCount = {
          'a':9, 'b':2 ,'c':2 ,
          'd':4 ,'e':12 ,'f':2 ,
          'g':3 ,'h':2 ,'i':9 ,
          'j':1 ,'k':1 ,'l':4 ,
          'm':2 ,'n':6 ,'o':8 ,
          'p':2 ,'q':1 ,'r':6,
          's':4 ,'t':6 ,'u':4 ,
          'v':2 ,'w':2 ,'x':1 ,'y':2 ,'z':1,'BLANK':2
         }
        for k,v in tileCount.iteritems():
            for i in xrange(1,v+1):
                self.tiles.append(Tile(k))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.tiles)

    def newHand(self):
        out = []
        for i in xrange(0,7):
            out.append(self.tiles.pop())
        return out
        
    def isEmpty(self):
        return len(self.tiles) == 0
    
    def putBack(self,tile):
        self.tiles.append(tile)
        shuffle()
    
    def getTile(self,n=1):
        out = []
        for i in xrange(1,n+1):
            out.append(self.tiles.pop())
        return out
    
class Tile(Scores.Scores):
    def __init__(self,label):
        self.label = label
        self.score = self.scoreLetter(label)
    def __str__(self):
        return str((self.label,self.score))
t = Bag()
