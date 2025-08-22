cards = ["2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad",
         "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac",
         "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah",
         "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As"]

def ResetProbabilities():
    global HighCard, Pair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush, RoyalFlush, CommunityCardStatus
    HighCard = ""
    Pair = 0
    TwoPair = 0
    ThreeOfAKind = 0
    Straight = 0
    Flush = 0
    FullHouse = 0
    FourOfAKind = 0
    StraightFlush = 0
    RoyalFlush = 0
    CommunityCardStatus = 0

def HighCardDisplay():
    pass

def PairProbability():
    pass

def TwoPairProbability():
    pass

def ThreeOfAKindProbability():
    pass

def StraightProbability():
    pass

def FlushProbability():
    pass

def FullHouseProbability():
    pass

def FourOfAKindProbability():
    pass

def StraightFlushProbability():
    pass

def RoyalFlushProbability():
    pass

def ProbabilityDisplay():
    pass


while True:
    ResetProbabilities()
