# Deck Data Compiler v1.0
# Last update: 12/10/18
# Thomas Barnett and Samyak Jain
# thomasbarnett2021@u.northwestern.edu & samyakjain2021@u.northwestern.edu
# Individual files are included to run each segment if desired

import os
import time
import scrython


def process():
        # NOTE: Must replace file paths for users computer
        # Decks placed in three folders, based on classifier
    pathOutput = '/Users/Tom/desktop/Output/processedDecks.txt'
    outputFile = open(pathOutput, "a")

    pathInput = '/Users/Tom/desktop/aggro/'
    classifier = "Aggro"
    read_folder(outputFile, pathInput, classifier)

    pathInput = '/Users/Tom/desktop/midrange/'
    classifier = "Midrange"
    read_folder(outputFile, pathInput, classifier)

    pathInput = '/Users/Tom/desktop/control/'
    classifier = "Control"
    read_folder(outputFile, pathInput, classifier)

    pathInput = '/Users/Tom/desktop/Output/processedDecks.txt'
    inputFile = open(pathInput, "r")
    pathOutput = '/Users/Tom/desktop/Output/scryfalledDecks.txt'
    outputFile = open(pathOutput, "a")
    ID3Output = '/Users/Tom/desktop/Output/ID3process.txt'
    ID3file = open(ID3Output, "a")

    parseInputFile(inputFile, outputFile, ID3file)

    pathInput = '/Users/Tom/desktop/Output/ID3process.txt'
    inputFile = open(pathInput, "r")
    pathOutput = '/Users/Tom/desktop/Output/WEKAprocess.csv'
    outputFile = open(pathOutput, "a")

    parseInputFileForWeka(inputFile, outputFile)

    pathInput = '/Users/Tom/desktop/Output/processedDecks.txt'

    pathOutput = '/Users/Tom/desktop/Output/BagWEKA.csv'
    outputFile = open(pathOutput, "a")

    list_all_cards(pathInput)
    append_cards(pathInput, outputFile)

    pathInput = '/Users/Tom/desktop/Output/processedDecks.txt'

    pathOutput = '/Users/Tom/desktop/Output/BagWEKA.csv'
    outputFile = open(pathOutput, "a")

    list_all_cards(pathInput)
    append_cards(pathInput, outputFile)



def read_folder(outputFile, pathInput, classifier):

    # Compiles the three folders of data from MTGTop8 into one text file
    files = os.listdir(pathInput)
    for name in files:
        if ".txt" in name:
            outputFile.write("Class " + classifier)
            read_file(pathInput, outputFile, name)
            outputFile.write('\n')



def read_file(pathInput, outputFile, name):
    # Separates cards with |, removes sideboard

    pathInput = pathInput + name
    print(pathInput)
    inputFile = open(pathInput, "r")
    for line in inputFile:
        if "Sideboard" in line:
            break
        outputFile.write("|" + line.rstrip('\n'))
    inputFile.close()

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

    # Fetches all of the data from Scryfall
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

def parseInputFileForWeka(inputFile,outputFile):

    # Writes classifiers at the top
    outputFile.write("Class,AvgCMC,Creatures,Lands,Instants,Sorcerys,Enchantments,Artifacts,Planeswalkers,Red,Blue,Black,White,Green")
    outputFile.write('\n')

    for line in inputFile:
        parseDeckForWeka(line, outputFile)
        outputFile.write('\n')

def parseDeckForWeka(line,outputFile):
    deck = line.split('|')

    for card in deck:
        splitString = card.split(' ', 1)
        outputFile.write(splitString[1].strip('\n') + ",")


def parseDeckForBag(line):
    #Creates bag of words output

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


def list_all_cards(pathInput):
    cards = open(pathInput, "r")

    for line in cards:
        parseDeckForBag(line)

    cards.close()


if __name__ == "__main__":
    process()