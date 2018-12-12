def process():
    pathInput = '/Users/Tom/desktop/Output/ID3process.txt'
    inputFile = open(pathInput, "r")
    pathOutput = '/Users/Tom/desktop/Output/WEKAprocess.csv'
    outputFile = open(pathOutput, "a")

    parseInputFile(inputFile,outputFile)


def parseInputFile(inputFile,outputFile):

    outputFile.write("Class,AvgCMC,Creatures,Lands,Instants,Sorcerys,Enchantments,Artifacts,Planeswalkers,Red,Blue,"
                     "Black,White,Green")
    outputFile.write('\n')

    for line in inputFile:
        parseDeck(line, outputFile)
        outputFile.write('\n')

def parseDeck(line,outputFile):
    deck = line.split('|')

    for card in deck:
        splitString = card.split(' ', 1)
        outputFile.write(splitString[1].strip('\n') + ",")


if __name__ == "__main__":
        process()