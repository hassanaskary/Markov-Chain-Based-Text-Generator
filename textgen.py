import numpy as np
import random
import re


def insertData(file_name):
    with open(file_name, "r") as f:
        read_data = f.read()
    return read_data


def makeEdgeMatrix(read_data):
    # read_data but put into a list seperated by spaces.
    read_data_list = read_data.split()
    list_of_words = []  # this list contains all the words, once.
    initial_words = []  # list of words that come at the start of a sentence.

    for w in read_data_list:
        # populating list_of_words
        if w not in list_of_words:
            list_of_words.append(w)

    number_of_words = len(list_of_words)

    # (len(read_data_list)-1) is so that loop stops at n-2 if n is the size of read_data_list. This so that initial_words.append doesn't throw index out of bounds errors
    for c in range(len(read_data_list)-1):
        # populating initial_words
        search_string = read_data_list[c]  # stores current word in a variable
        # check if search_string is an ending word which containes '.','!', or '?' at the end of it
        if re.search(r"[.?!]", search_string):
            # if it is then append the next word to initial_words
            initial_words.append(read_data_list[c+1])

    edge_matrix = np.zeros((number_of_words, number_of_words))

    # temporary list that contains the immediate right words of current word being considered.
    list_of_adjacent_words = []

    # TODO should be able to iterate through the list once.
    # when ever a word is found add the immediate right word to matrix
    # and also update probabilities for that word
    for i in list_of_words:  # current word being considered.
        # iterating over read_data_list to find matches
        for j in range(len(read_data_list)):
            if read_data_list[j] == i:  # if considered word if found.
                # and the next index is not out of bounds.
                if j+1 >= len(read_data_list):
                    break  # if it is then break
                # then put immediate right word into list_of_adjacent_words.
                list_of_adjacent_words.append(read_data_list[j+1])

        for k in list_of_adjacent_words:  # now to put values in edge matrix.
            # we're keeping track of location of words by their index. And the edge matrix contains probabilities.
            edge_matrix[list_of_words.index(i), list_of_words.index(
                k)] = list_of_adjacent_words.count(k)/len(list_of_adjacent_words)
        # clearing list so that it can store immediate right words of the next word.

        list_of_adjacent_words.clear()

    return edge_matrix, list_of_words, initial_words


def generateText(edge_matrix, list_of_words, initial_words):
    starting_word = random.choice(initial_words)
    current_word = ""
    next_word = ""
    text = ""
    text += starting_word + " "
    current_word = starting_word

    for _ in range(100):
        weights = edge_matrix[list_of_words.index(current_word), :]
        next_word = random.choices(list_of_words, weights, k=1)
        next_word = ''.join(next_word)
        text += (next_word + " ")
#        if re.search(r"[.?!]", text):
#            break
        current_word = next_word

    print(text)


def main():
    file_name = input("Enter name of txt file ('example.txt'): ") # ask for filename
    file_name = "text/" + file_name # adding text/ at start so that file is searched in text/ folder
    read_data = insertData(file_name) # parsing file
    edge_matrix, list_of_words, initial_words = makeEdgeMatrix(read_data) # making edge_matrix from read_data

    choice = "y" # user choice
    while(choice == "y"): # checking choice if 'y' then generate text if 'n' then terminate
        generateText(edge_matrix, list_of_words, initial_words) # generating text
        choice = input("Generate text? (y/n) ") # getting user choice


if __name__ == "__main__":
    main()
