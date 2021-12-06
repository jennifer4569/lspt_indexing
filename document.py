class Document(object):

    # constructor
    def __init__(self, name, numWords):
        self.docName = name
        self.numWords = numWords
        self.score = 0
        self.positionalInfo = {}

    def calculateDocScore(self, tokenInfo):
        weights = {
            "title": 1, 
            "headers": 2, 
            "links": 0,
            "other": 2
        }
        
        total = 0
        multiplier = 0
        for position, frequency in tokenInfo:
            # what weight each position has
            multiplier = weights.get(position, 0)
            total += multiplier * frequency
        
        # divide the total score by the number of words in the document so as to not favor larger documents    
        total /= self.numWords
            
        #if certain information isn't available
        if total == 0:
            raise Exception("Not enough information to calculate score")
        return total
    
    def getName(self):
        return self.docName
    
    def getScore(self):
        return self.score
    
    def setScore(self, newScore):
        self.score = newScore
        
    def setPositionalInfo(self, tokenInfo):
        self.positionalInfo = tokenInfo
        
    def getPositionalInfo(self):
        return self.positionalInfo