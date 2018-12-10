import numpy as np
import random

def insertData():
    with open("The_Count_of_Monte_Cristo_Chapter_1.txt", "r") as f:
        read_data = f.read()
    makeEdgeMatrix(read_data)

def makeEdgeMatrix(read_data):
    read_data_list = read_data.split() # read_data but put into a list seperated by spaces.
    list_of_words = [] # This list contains all the words, once.
    for w in read_data_list:
        if w not in list_of_words:
            list_of_words.append(w)
    number_of_words = len(list_of_words)
    edge_matrix = np.zeros((number_of_words, number_of_words))
    list_of_adjacent_words = [] # temporary list that contains the immediate right words of current word being considered.
    for i in list_of_words: # current word being considered.
        for j in range(len(read_data_list)):
            if read_data_list[j] == i: # if considered word if found.
                if j+1 >= len(read_data_list): # and the next index is not out of bounds.
                    break # if it is then break
                list_of_adjacent_words.append(read_data_list[j+1]) # then put immediate right word into list_of_adjacent_words.
        for k in list_of_adjacent_words: # now to put values in edge matrix.
            edge_matrix[list_of_words.index(i),list_of_words.index(k)] = list_of_adjacent_words.count(k)/len(list_of_adjacent_words) # we're keeping track of location of words by their index. And the edge matrix contains probabilities.
        list_of_adjacent_words.clear() # clearing list so that it can store immediate right words of the next word.
    generateSentences(edge_matrix, read_data_list, list_of_words)

def generateSentences(edge_matrix, read_data_list, list_of_words):
    starting_word = random.choice(read_data_list)
    current_word = ""
    next_word = ""
    sentence = ""
    sentence += starting_word + ""
    current_word = starting_word
    for i in range(100):
        weights = edge_matrix[list_of_words.index(current_word), : ]
        next_word = random.choices(list_of_words, weights, k=1)
        next_word = ''.join(next_word)
        sentence += (next_word + " ")
        current_word = next_word
    print(sentence)

def main():
    insertData()

if __name__=="__main__":
    main()