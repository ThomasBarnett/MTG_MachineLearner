
from tkinter import filedialog


def parse():
    filepath = "/Users/Tom/desktop/Output/ID3process.txt"
    file = open(filepath, 'r')

    output_array = []

    for line in file:
        output_array.append(read_deck(line))

    print(output_array)
    return output_array


def read_deck(line):
        attribute_array = line.split("|")
        ret_dict = {}

        for attribute in attribute_array:
            split_att = attribute.split(" ")
            ret_dict[split_att[0]] = split_att[1].strip('\n')

        return ret_dict


if __name__ == "__main__":
    # filepath = filedialog.askopenfilename()
    filepath = "/Users/Tom/desktop/Output/ID3process.txt"
    parse(filepath)

