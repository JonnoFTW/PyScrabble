## Class to make a prefix Trie. Stores each word as a sequence in the trie
## Trie takes a lines separated dictionary of words.
## Words can be looked up and their scrabble score returned
## otherwise None
import Scores
class Trie(Scores.Scores):
    # Build up a trie from a text file,
    # line separated
    def __init__(self,dict_file):
        self.root = TrieNode()
        with open(dict_file) as f:
            for line in f:
                self.insert(line.rstrip())
                
    # Insert a word into the trie
    def insert(self,word):
        node = self.root
        for i in word:
            node = node.addChild(i,TrieNode())
            node.setLabel(i)
        # Last element is a word
        node.isTerminal = True
        
    def lookup(self,word):
        node = self.root
        score = 0
        for i in word:
            i = i.lower()
            score += self.scoreLetter(i)
            node = node.getChild(i)
            if node == None:
                return (False,None)
        if not node.isTerminal:
            return (False,None)
        return (True,score)
    
    
    def printChildren(self):
        childs = [self.root]
        while(len(childs) > 0):
            t = childs.pop()
            for i in t.children:
                childs.append(i)
            for i in t.children:
                print i.getLabel(),' ',
            print
         
class TrieNode:
    def __init__(self):
        # Children is a set of nodes
        self.children = set()
        self.isTerminal = False
        self.score = 0
        
    def setLabel(self,label):
        self.label = label
    
    def getLabel(self):
        return self.label
    
    def getChild(self,label):
        for node in self.children:
            if node.getLabel() == label:
                return node
        return None
    
    def addChild(self,label,node):
        n = self.getChild(label)
        if n == None:
            self.children.add(node)
            return node
        return n
if __name__ == "__main__":
    t = Trie("ospd3.txt")
    print t.lookup("abacus")
    print t.lookup("null")
    print t.lookup("test")

