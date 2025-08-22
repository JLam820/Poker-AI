# Card Deck -------------------------------------------------------------------------------------------------
cards = ["2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad",
         "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac",
         "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah",
         "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As"]

# Probability Functions -------------------------------------------------------------------------------------
def HighCardDisplay(holecards, communityCards, deck, Probability, CommunityCardStatus):
    cardValues = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    CardPool = holecards + communityCards
    rankedCards = []
    highCardString = ""

    if any(prob == 100 for prob in Probability[1:]):
        Probability[0] = "N/A"
        return

    for card in CardPool:
        cardValue = [cardValues[card[0]], card]
        rankedCards.append(cardValue)
    rankedCards.append([0, ""])
    rankedCards.sort(reverse=True, key=lambda x: x[0])

    for i in range(5):
        if rankedCards[i][0] == 0:
            break
        else:
            highCardString += rankedCards[i][1] + " "

    Probability[0] = highCardString.strip()


def PairProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    CardPool = holecards + communityCards
    
    rank_counts = {}
    for card in CardPool:
        rank = card[0]
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    has_duplicate_rank = any(count >= 2 for count in rank_counts.values())
    
    if has_duplicate_rank:
        Probability[1] = 100
        return
    
    if CommunityCardStatus == 0:
        remainingCards = len(deck)
        
        prob_no_pair = 1.0
        cards_to_avoid = 6
        
        for i in range(5):
            prob_no_pair *= (remainingCards - cards_to_avoid) / remainingCards
            remainingCards -= 1
            cards_to_avoid += 3

        probPair = (1 - prob_no_pair) * 100
        Probability[1] = round(probPair, 2)
    
    elif CommunityCardStatus == 1:
        remainingCards = len(deck)

        prob_no_pair = 1.0
        cards_to_avoid = 15

        for i in range(2):
            prob_no_pair *= (remainingCards - cards_to_avoid) / remainingCards
            remainingCards -= 1
            cards_to_avoid += 3

        probPair = (1 - prob_no_pair) * 100
        Probability[1] = round(probPair, 2)

    elif CommunityCardStatus == 2:
        remainingCards = len(deck)

        prob_no_pair = 1.0
        cards_to_avoid = 18

        prob_no_pair *= (remainingCards - cards_to_avoid) / remainingCards

        probPair = (1 - prob_no_pair) * 100
        Probability[1] = round(probPair, 2)

    else:
        Probability[1] = 0.0



def TwoPairProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    pass


def ThreeOfAKindProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    pass


def StraightProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    pass


def FlushProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    pass


def FullHouseProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    pass


def FourOfAKindProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    pass


def StraightFlushProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    pass


def RoyalFlushProbability(holecards, communityCards, deck, Probability, CommunityCardStatus):
    pass


# Calcuate and Display Probability ---------------------------------------------------------------------------------------
def ProbabilityDisplay(holeCards, communityCards, Probability, CommunityCardStatus):
    stages = {
        0: "Pre-Flop",
        1: "Flop",
        2: "Turn",
        3: "River"
    }

    print()
    print("===============================================")
    print("Stage:", stages[CommunityCardStatus])
    print("Hole Cards:", holeCards)
    print("Community Cards:", communityCards)
    print("-----------------------------------------------")
    print("Probabilities:")
    print("High Card:", Probability[0])
    print("One Pair:", Probability[1])
    print("Two Pair:", Probability[2])
    print("Three of a Kind:", Probability[3])
    print("Straight:", Probability[4])
    print("Flush:", Probability[5])
    print("Full House:", Probability[6])
    print("Four of a Kind:", Probability[7])
    print("Straight Flush:", Probability[8])
    print("Royal Flush:", Probability[9])
    print("===============================================")
    print()


def CalculateProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus):
    
    PairProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    TwoPairProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    ThreeOfAKindProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    StraightProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    FlushProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    FullHouseProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    FourOfAKindProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    StraightFlushProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    RoyalFlushProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus)
    HighCardDisplay(holeCards, communityCards, deck, Probability, CommunityCardStatus)


# Card Input Functions --------------------------------------------------------------------------------------
def holeCardsInput(holeCards, deck):
    flag = True
    while flag:
        holeCardsInputed = input("Enter your hole cards: ").strip().split()
        if len(holeCardsInputed) != 2 or any(card not in deck for card in holeCardsInputed):
            print("Invalid input. Please enter two valid hole cards.")
        else:
            holeCards.extend(holeCardsInputed)
            deck.remove(holeCardsInputed[0])
            deck.remove(holeCardsInputed[1])
            flag = False
    return holeCards


def communityCardsInput(communityCards, deck, CommunityCardStatus):

    flag = True
    while flag:
        if CommunityCardStatus == 1:
            cards_needed = 3
            prompt = "Enter the 3 community cards (flop): "
        elif CommunityCardStatus == 2:
            cards_needed = 1
            prompt = "Enter the turn card: "
        elif CommunityCardStatus == 3:
            cards_needed = 1
            prompt = "Enter the river card: "

        new_cards = input(prompt).strip().split()
        if len(new_cards) != cards_needed or any(card not in deck for card in new_cards):
            print(f"Invalid input. Please enter {cards_needed} valid community card(s).")
        else:
            communityCards.extend(new_cards)
            for card in new_cards:
                deck.remove(card)
            flag = False
        return communityCards


# Main Program Loop -----------------------------------------------------------------------------------------
while True:
    Probability = ["", 0, 0, 0, 0, 0, 0, 0, 0, 0]
    CommunityCardStatus = 0
    holeCards = []
    communityCards = []
    deck = cards.copy()


    while CommunityCardStatus <= 3:
        if CommunityCardStatus == 0:
            holeCards = holeCardsInput(holeCards, deck)     
        else:
            communityCards = communityCardsInput(communityCards, deck, CommunityCardStatus)

        CalculateProbability(holeCards, communityCards, deck, Probability, CommunityCardStatus) 
        ProbabilityDisplay(holeCards, communityCards, Probability, CommunityCardStatus)
        CommunityCardStatus += 1


    play_again = input("Play another hand? (y/n): ").lower()
    if play_again != 'y':
        break
