class Player:
    def __init__(self,name,bag,dictionary,bot=None):
        self.tiles = []
        self.name  = name
        self.bag = bag
        self.d = dictionary
        self.score = 0

    def turn(self):
        if self.bot:
            self.chooseTurn()
            return
        for i in self.tiles:
            print i
        play = raw_input('Discard (d), pass (p), Play word (w) ')
        if play == 'd':
            print zip(self.tiles,range(0,len(self.tiles)))
            out = raw_input('Which number tiles to remove? ')
            disc = []
            for i in out.split():
                try:
                    disc.append(int(i))
                except Exception, e:
                    print str(e)
            self.discard(disc)
            print "Your new tiles are: "+str(self.tiles)
            return
        elif play == 'p':
            return
        else:
            while True:
              try:
                place = raw_input('Where will the start of your letters be placed (x,y)\n (h(orizontal) v(ertical) d(iagonally)? ')
                x = int(place.split()[0])
                y = int(place.split()[1])
                direction = place.split()[2][0]
                break
              except:
                  print "formatting error, place it as 1 2 d
            word = raw_input('Which word would you like to play? ')
            #check if the player has the characters in their hand or they are on the board already
            while not self.inTiles(word) or not self.d.lookup(word)[0]:
                word = raw_input('That is not a valid word ')
            print word+' scores '+str(self.d.lookup(word)[1])
            
            
            
    def inTiles(self,word):
        letters = []
        for i in self.tiles:
            letters.append(i.label)
        for i in word:
            try:
                letters.remove(i)
            except:
                return False
        return True

    def playable(self,x,y,word,direction):
        """
        Determines if a word can be placed on the board by
         1. Placing them down at the specified starting position
            skipping over any tiles already on the board and keeping
            track of where tiles have been placed
         2. Finding the word that has been created
         3a. If this is word is actually a word, keep it on there or
         3b. Remove the placed tiles and have the word replaced
        """
        if direction == "h":
            pass
        elif direction == "v":
            pass
        elif direction == "d":
            pass
        else:
            raise NotPlayable("Word '%s' cannot be placed" % word)
        
    def discard(self,c):
        for i in c:
            self.bag.putBack(self.tiles[i])
            self.tiles[i] = self.bag.getTile()
        return 
    
    def newHand(self):
        for i in self.tiles:
            self.bag.putBack(i)
        self.tiles = self.bag.newHand()

    def chooseTurn():
        pass
            

class NotPlayable(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
