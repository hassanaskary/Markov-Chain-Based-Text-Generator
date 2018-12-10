import numpy as np

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
    
    print(edge_matrix)

def main():
    insertData()

if __name__=="__main__":
    main()