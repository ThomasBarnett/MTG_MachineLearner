all_cards = []

def process():

    pathInput = '/Users/Tom/desktop/Output/processedDecks.txt'

    pathOutput = '/Users/Tom/desktop/Output/BagWEKA.csv'
    outputFile = open(pathOutput, "a")

    list_all_cards(pathInput)
    append_cards(pathInput, outputFile)


def list_all_cards(pathInput):
    cards = open(pathInput, "r")

    for line in cards:
        parseDeckForBag(line)

    cards.close()


def parseDeckForBag(line):
    deck = line.split('|')

    global all_cards

    for card in deck:
        if "Class " not in card:
            splitString = card.split(' ', 1)
            if(all_cards.count(splitString[1].strip('\n')) == 0):
                all_cards.append(splitString[1].strip('\n'))


def append_cards(pathInput, outputFile):
    cards = open(pathInput, "r")

    outputFile.write("Class,")

    for card in all_cards:
        outputFile.write(card.replace(',','') + ",")

    outputFile.write('\n')

    for line in cards:
        parseCardsForBag(line, outputFile)
        outputFile.write('\n')

def parseCardsForBag(line,outputFile):
    global all_cards
    freq_cards = []

    for i in range(0,len(all_cards)):
        freq_cards.append('0')

    deck = line.split('|')

    for card in deck:
        if "Class " in card:
            splitString = card.split(' ', 1)
            outputFile.write(splitString[1].strip('\n') + ",")
        else:
            splitString = card.split(' ', 1)
            index = all_cards.index(splitString[1].strip('\n'))
            freq_cards[index] = splitString[0]

    for card in freq_cards:
        outputFile.write(card + ",")


if __name__ == "__main__":
        process()