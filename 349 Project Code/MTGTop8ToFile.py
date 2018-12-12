import os


def process():
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


def read_folder(outputFile, pathInput, classifier):


    files = os.listdir(pathInput)
    for name in files:
        if ".txt" in name:
            outputFile.write("Class " + classifier)
            read_file(pathInput, outputFile, name)
            outputFile.write('\n')



def read_file(pathInput, outputFile, name):

    pathInput = pathInput + name
    print(pathInput)
    inputFile = open(pathInput, "r")
    for line in inputFile:
        if "Sideboard" in line:
            break
        outputFile.write("|" + line.rstrip('\n'))
    inputFile.close()


if __name__ == "__main__":
    process()

