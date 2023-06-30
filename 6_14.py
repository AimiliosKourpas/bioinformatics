#|-----------------------------------|#
#|         BioInformatics 2023       |#
#|-----------------------------------|#
#|    Aimilianos Kourpas             |#
#|    Anastasis Melaxroinidis        |#
#|-----------------------------------|#

import random
from Bio import SeqIO

def make_move(liver_len, brain_len): # function move with 2 parameters
    if liver_len == 1: # if liver_len is 1
        return liver_len - 1, brain_len - 2 # return liver_len - 1, brain_len - 2
    elif brain_len == 1: # if brain_len is 1
        return liver_len - 2, brain_len - 1 # return liver_len - 2, brain_len - 1

    removal_pick = random.randint(0, 1) # removal_pick = random.randint(0, 1)
    return liver_len - removal_pick - 1, brain_len - (1 - removal_pick) - 1 # return liver_len - removal_pick - 1, brain_len - (1 - removal_pick) - 1



liver_sequences = list(SeqIO.parse("liver.fna", "fasta"))
brain_sequences = list(SeqIO.parse("brain.fna", "fasta"))

if len(liver_sequences) == 0 or len(brain_sequences) == 0:
    print("Error: No sequences found in the input files.")
else:
    liver_seq = liver_sequences[0].seq
    brain_seq = brain_sequences[0].seq

    liver_len = len(liver_seq)
    brain_len = len(brain_seq)

    print("Initial lengths = liver length:", liver_len, "brain length:", brain_len)

    counter = 0
    while (liver_len >= 2 and brain_len >= 1) or (liver_len >= 1 and brain_len >= 2):
        current_player = "First Player" if counter % 2 == 0 else "Second Player"

        liver_len, brain_len = make_move(liver_len, brain_len)

        if counter < 3 or counter >= 20000:
            print("\nPlays:", current_player)
            print("Liver length:", liver_len, "-||- Brain length:", brain_len)
        elif counter == 3:
            print("...")
            print("...")
            print("...")
            print("...")

        counter += 1

    winner = "Second Player" if counter % 2 == 0 else "First Player"
    print("\n" , winner, "is the WINNER")
