class Document(object):
    #tokens is a dictionary

    # constructor
    def __init__(self, name, numWords):
        self.docName = name
        self.numWords = numWords
        self.tokens = {}

    def calculateScore(self, tokenInfo):
        weights = {
            "title": 1.0, 
            "headers": 0.75, 
            "links": 0.5,
            "other": 0.25
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

    def addToken(self, tokenName, positionInfo):
        score = calculateScore(positionInfo)
        self.tokens[tokenName] = (positionInfo, score)
    
    def getTokenInfo(self, tokenName):
        return self.tokens[tokenName]

