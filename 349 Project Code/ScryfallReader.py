import scrython
import time

def process():
    pathInput = '/Users/Tom/desktop/Output/processedDecks.txt'
    inputFile = open(pathInput, "r")
    pathOutput = '/Users/Tom/desktop/Output/scryfalledDecks.txt'
    outputFile = open(pathOutput, "a")
    ID3Output = '/Users/Tom/desktop/Output/ID3process.txt'
    ID3file = open(ID3Output, "a")

    parseInputFile(inputFile,outputFile,ID3file)

def parseInputFile(inputFile,outputFile,ID3file):

    for line in inputFile:
        parseDeck(line, outputFile,ID3file)
        outputFile.write('\n')
        ID3file.write('\n')


def parseDeck(line,outputFile,ID3file):
    deck = line.split('|')
    avgCmc = 0
    creatureCount = 0
    landCount = 0
    instantCount = 0
    sorceryCount = 0
    enchantmentCount = 0
    planeswalkerCount = 0
    artifactCount = 0
    red = 0
    blue = 0
    green = 0
    white = 0
    black = 0


    for card in deck:
        outputFile.write(card.strip('\n') + "|")

        if "Class " in card:
            ID3file.write(card + "|")
        else:

            splitString = card.split(' ', 1)
            rtrnArray = fetchCard(splitString[1])
            numOfCard = int(splitString[0])
            avgCmc = avgCmc + rtrnArray[0] * numOfCard

            if "Creature" in rtrnArray[1]:
                creatureCount = creatureCount + numOfCard
            if "Instant" in rtrnArray[1]:
                instantCount = instantCount + numOfCard
            elif "Sorcery" in rtrnArray[1]:
                sorceryCount = sorceryCount + numOfCard
            if "Artifact" in rtrnArray[1]:
                artifactCount = artifactCount + numOfCard
            elif "Enchantment" in rtrnArray[1]:
                enchantmentCount = enchantmentCount + numOfCard
            elif "Land" in rtrnArray[1]:
                landCount = landCount + numOfCard
            if "Planeswalker" in rtrnArray[1]:
                planeswalkerCount = planeswalkerCount + numOfCard

            red = red + (len(rtrnArray[2].split('R')) - 1)*numOfCard
            blue = blue + (len(rtrnArray[2].split('U')) - 1)*numOfCard
            black = black + (len(rtrnArray[2].split('B')) - 1)*numOfCard
            white = white + (len(rtrnArray[2].split('W')) - 1)*numOfCard
            green = green + (len(rtrnArray[2].split('G')) - 1)*numOfCard

    outputFile.write("AvgCMC " + str((avgCmc/(60-landCount))) + "|")
    outputFile.write("Creatures " + str(creatureCount) + "|")
    outputFile.write("Lands " + str(landCount) + "|")
    outputFile.write("Instants " + str(instantCount) + "|")
    outputFile.write("Sorcerys " + str(sorceryCount) + "|")
    outputFile.write("Enchantments " + str(enchantmentCount) + "|")
    outputFile.write("Artifacts " + str(artifactCount) + "|")
    outputFile.write("Planeswalkers " + str(planeswalkerCount) + "|")
    outputFile.write("Red " + str(red) + "|")
    outputFile.write("Blue " + str(blue) + "|")
    outputFile.write("Black " + str(black) + "|")
    outputFile.write("White " + str(white) + "|")
    outputFile.write("Green " + str(green))

    ID3file.write("AvgCMC " + str((avgCmc / (60 - landCount))) + "|")
    ID3file.write("Creatures " + str(creatureCount) + "|")
    ID3file.write("Lands " + str(landCount) + "|")
    ID3file.write("Instants " + str(instantCount) + "|")
    ID3file.write("Sorcerys " + str(sorceryCount) + "|")
    ID3file.write("Enchantments " + str(enchantmentCount) + "|")
    ID3file.write("Artifacts " + str(artifactCount) + "|")
    ID3file.write("Planeswalkers " + str(planeswalkerCount) + "|")
    ID3file.write("Red " + str(red) + "|")
    ID3file.write("Blue " + str(blue) + "|")
    ID3file.write("Black " + str(black) + "|")
    ID3file.write("White " + str(white) + "|")
    ID3file.write("Green " + str(green))




def fetchCard(name):
    time.sleep(0.1)
    card = scrython.cards.Named(fuzzy=name)

    if "transform" in card.layout():
        rtrnArray = [card.cmc(), card.type_line(), card.card_faces()[0]["mana_cost"]]
    else:
        rtrnArray = [card.cmc(), card.type_line(), card.mana_cost()]

    return rtrnArray

if __name__ == "__main__":
    process()
    print("done")
