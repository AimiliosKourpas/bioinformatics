#|-----------------------------------|#
#|         BioInformatics 2023       |#
#|-----------------------------------|#
#|    Aimilianos Kourpas             |#
#|    Anastasis Melaxroinidis        |#
#|-----------------------------------|#


def loadSeq(txtName): # function loadSeq with 1 parameter
    print("Loading the file " + txtName ) # print the txtName 
    with open(txtName, "r") as seqFile: #r = read mode 
        seq = [letter for line in seqFile for letter in line] #list comprehension 
    return seq 


def validate_input(prompt, valid_values, seq): # function  validate_input with 3 parameters
    while True: # while True
        user_input = input(prompt) # user_input = input(prompt)
        if user_input in valid_values and user_input != seq: # if user_input is in valid_values and user_input is not seq1
            return user_input # return user_input
        print("Invalid input or seq1 and seq2 are the same.Try again!") #error message 


def game(seq1, seq2): # example seq1 = brain.txt , seq2 = liver.txt
    seq1 = loadSeq(seq1) # seq1
    seq2 = loadSeq(seq2) # seq2

    canWin = [False, True] # list of booleans
    winning = [] # list of winning splits

    for i in range(2, len(seq1) + 1): # a for loop that iterates over the range of 2 to len(seq1) + 1
        for j in range(1, i // 2 + 1):  #a for loop that iterates over the range of 1 to i // 2 + 1
            if not canWin[j] and not canWin[i - j]: # if canWin[j] is False and canWin[i - j] is False
                canWin.append(True)     # append True to canWin
                winning.append([j, i - j]) # append [j, i - j] to winningRmv
                break
        else:
            canWin.append(False) # append False to canWin

    winner = "A" if canWin[-1] or canWin[len(seq2)] else "B" 

    print(f"The winner is {winner}")
    print("The winning splits:")
    for split in winning:
        print(split)


seq = ["brain.fna", "liver.fna", "muscle.fna"]

seq1 = validate_input("Choose the first Sequence (1-brain, 2-liver, 3-muscle): ",["1", "2", "3"], "") 

seq2 = validate_input("Choose the second Sequence (1-brain, 2-liver, 3-muscle): ",["1", "2", "3"], seq1)

game(seq[int(seq1) - 1], seq[int(seq2) - 1])

