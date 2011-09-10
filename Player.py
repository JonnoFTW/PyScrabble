class Player:
    def __init__(self,name,bag,dictionary,bot=None):
        self.tiles = []
        self.name  = name
        self.bag = bag
        self.d = dictionary
        self.score = 0

    def turn(self):
        for i in self.tiles:
            print i
        play = raw_input('Discard (d), pass (p), Play word (w) ')
        if play == 'd':
            out = raw_input('Which tiles to remove? ')
            for i in out.split():
                discard(self.tiles.index())
            return
        elif play == 'p':
            return
        else:
            word = raw_input('Which word would you like to play? ')
            #check if the player has the characters in their hand
            while not self.playable(word) and not self.d.lookup(word)[0]:
                word = raw_input('That is not a valid word ')
            print word+' scores '+str(self.d.lookup(word)[1])
            print 'place where?'
    def playable(self,word):
        letters = []
        for i in self.tiles:
            letters.append(i.label)
        for i in word:
            try:
                letters.remove(i)
            except:
                return False
        return True        
        
        
        
    def discard(self,c):
        self.bag.putBack(self.tiles.pop(c))
        return 
    
    def newHand(self):
        for i in self.tiles:
            self.bag.putBack(i)
        self.tiles = self.bag.newHand()
            
        
