class Piece:

    alliance = None
    position = None
    img = None

    def __init__(self):
        pass
    
    def toString(self):
        return self.__class__.__name__

    def getImg(self):
        return self.img

class NullPiece(Piece):
    pass


class Flag(Piece):

    available = 1

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"
        self.taken = False
       
    def getAlliance():
        return alliance

    def getImg():
        return img

class Grenade(Piece):

    rank = 0
    available = 2

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class Landmine(Piece):

    rank = 0
    available = 3

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img
    
class Marshal(Piece):

    rank = 1
    available = 1

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class General(Piece):

    rank = 2
    available = 1

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class Lieutenant(Piece):

    rank = 3
    available = 2

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class Brigadier(Piece):

    rank = 4
    available = 2

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class Colonel(Piece):

    rank = 5
    available = 2

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class Major(Piece):

    rank = 6
    available = 2

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class Captain(Piece):

    rank = 7
    available = 3

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class Commander(Piece):

    rank = 8
    available = 3

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img

class Engineer(Piece):

    rank = 9
    available = 3

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
        self.img = "bin\\"+ self.toString() +".png"

    def getAlliance():
        return alliance

    def getRank():
        return rank

    def getImg():
        return img
