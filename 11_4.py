#|-----------------------------------|#
#|         BioInformatics 2023       |#
#|-----------------------------------|#
#|   Aimilianos Kourpas              |#
#|   Anastasis Melaxroinidis         |#
#|-----------------------------------|#

import numpy as np # Import numpy library

def viterbi(observation, emissions, states, A, B, P): # Viterbi function with 6 parameters 
    scores = np.zeros((len(observation), len(states))) # Create a matrix with zeros with dimensions T x len(states)
    backpointers = np.zeros((len(observation), len(states)), dtype=int) # Create a matrix with zeros with dimensions T x len(states) and is int type 

    scores[0] = P + B[emissions.index(observation[0])] # Calculate the scores for the first observation  

    for t in range(1,len(observation)): #a for loop from 1 to T 
        for j, state in enumerate(states): #a for loop with enumerate(states)
            transition_scores = scores[t - 1] + A[:, j] # Calculate the transition scores for the current stat
            max_score_index = np.argmax(transition_scores) # Find the index of the maximum transition score
            scores[t, j] = transition_scores[max_score_index] + B[emissions.index(observation[t]), j] # Calculate the score for the current state
            backpointers[t, j] = max_score_index # Save the index of the maximum transition score

    best_path = [np.argmax(scores[-1])] # Find the index of the maximum score for the last observation
    for t in range(len(observation) - 2, -1, -1): #a for loop from T - 2 to -1 with step -1
        best_path.insert(0, backpointers[t + 1, best_path[0]]) # Insert the index of the maximum transition score at the beginning of the best path

    return best_path, scores # Return the best path and the scores

emissions = ['A', 'G', 'T', 'C'] # Emissions
states = ['a', 'b'] # States

# Transition matrix
transition_prob = np.array([[0.9, 0.1], 
                            [0.1, 0.9]]) # a list of lists

# Emission matrix
emission_prob = np.array([[0.4, 0.2],
                          [0.4, 0.2],
                          [0.1, 0.3],
                          [0.1, 0.3]]) #a list of lists

# Initial probabilities
initial_prob = np.array([0.5, 0.5])
observation = 'GGCT' 

# Convert the probabilities to log2 probabilities
transition_prob_log = np.log2(transition_prob)
emission_prob_log = np.log2(emission_prob)
initial_prob_log = np.log2(initial_prob)

# Run the Viterbi algorithm and get the best path and the scores
best_path, scores = viterbi(observation, emissions, states, transition_prob_log, emission_prob_log, initial_prob_log)

# Print the scores
print("\nScores: \n")
for i in range(len(observation)): #a for loop from 0 to len(observation) 
    print(f"Step {i+1}: {', '.join(f'{states[j]}: {scores[i][j]:.3f}' for j in range(len(states)))}") # Print the scores for each state with f strings
 
print("\nBest_path: \n") 
# Print the best path
for i, state in enumerate(best_path): #a for loop with enumerate(best_path)
    print(f"Step {i+1}: {states[state]}") # Print the best path with f string

print("\nThe best path for ", observation, "is:", ' '.join(states[state] for state in best_path)) # Print the best path with f string

