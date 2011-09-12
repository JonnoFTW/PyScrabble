import Trie
from Bag import Bag
from Player import Player
from Board import  Board

##import pygtk
##pygtk.require('2.0')
##import gtk

class Game:
##    def main(self):
##        gtk.main()
    def delete_event(self, widget,event, data=None):
        return False
            
    def destroy(self, widget, data=None):
        gtk.main_quit()
        return False
    
    def __init__(self,d):
##        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
##        self.window.set_size_request(600,650)
##        self.window.set_title("Scrabble")
##        self.statusbar = gtk.Statusbar()
##        self.window.connect("delete_event",self.delete_event)
##        self.window.connect("destroy",self.destroy)
##        
##        self.window.show()
##        self.refresh()
        self.d = d
        self.bag = Bag()
        self.board = Board()
        self.players = []
        self.p1 = Player(raw_input("Player name: "),self.bag,self.d)
        self.p2 = Player("Robot",self.bag,self.d)
        for i in [self.p1,self.p2]:
            self.players.append(i)
        for i in self.players:
            i.newHand()

        while not self.bag.isEmpty():
            for i in self.players:
                print self.board
                print i.name+"'s turn"          
                i.turn()
        for i in self.players:
            print i.name+' '+str(i.score)
        

if __name__ == "__main__":
    d = Trie.Trie("dict.txt")
    while True:
        g = Game(d)
        g.main()
        if raw_input("play again? y/n ").lower() == "n":
            break
