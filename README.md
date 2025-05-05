# 🧬 Bioinformatics 

📍 **University of Piraeus**
📍 **Department of Informatics**
📅 Academic Year: 2022 – 2023
📘 Course: *Bioinformatics*
📈 Semester: 6th

---

## 📂 Table of Contents

* [Topic 1](#topic-1)
* [Topic 2](#topic-2)
* [Topic 3](#topic-3)
* [References](#references)

---

## 🧪 Topic 1: Decoding the Most Probable State Sequence in an HMM

### 📜 Problem Statement

Given an HMM with two states, α and β:

* State α favors purines (A, G)
* State β favors pyrimidines (C, T)
  The goal is to decode the most probable state sequence (α/β) for the observed sequence **GGCT** using logarithmic scores instead of raw probabilities.

### 🛠 Solution Overview

We apply the **Viterbi algorithm** 🛤, which uses dynamic programming to find the most probable path of hidden states by:
 - Using logarithmic probabilities to avoid underflow
 - Tracking scores and backpointers for each state
 - Performing backtracking to reconstruct the optimal path

### 💻 Implementation Details

* **Language**: Python 🐍
* **Library**: NumPy
* **Main Components**:

  * `emissions`: list of emission symbols
  * `states`: list of states
  * `transition_prob`: NumPy matrix of transition probabilities
  * `emission_prob`: NumPy matrix of emission probabilities
  * `initial_prob`: initial state probabilities
  * `scores`, `backpointers`: dynamic programming tables
  * `Viterbi`: main function implementing the algorithm

### ▶️ How to Run

1️⃣ Install Python and NumPy (`pip install numpy`)
2️⃣ Navigate to the directory containing `11_4.py`
3️⃣ Run:

```bash
python3 11_4.py
```

---

## 🎮 Topic 2: Winning Strategy in a Two-Sequence Game

### 📜 Problem Statement

Two players play a game with two “chromosomes” of length *n* and *m*.
On each turn, a player can:

* Destroy one chromosome
* Split the other into two non-empty parts
  The player who removes the last nucleotide wins.

### 🛠 Solution Overview

- Read sequences from `.fna` files
- Use logical lists (`canWin`, `winning`) to track win conditions
- Determine which moves lead to victory by simulating all possible splits
- Print the winning splits and identify the winner

### 💻 Implementation Details

* **Language**: Python 🐍
* **Functions**:

  * `loadSeq`: loads a sequence from a file
  * `validateInput`: checks user input
  * `game`: runs the main game loop

### ▶️ How to Run

1️⃣ Install Python
2️⃣ Navigate to the directory containing `6_12.py`
3️⃣ Run:

```bash
python3 6_12.py
```

---

## 🧩 Topic 3: Advanced Two-Sequence Game Strategy

### 📜 Problem Statement

Two players play with two sequences (*n*, *m* nucleotides).
On each turn, a player removes:

* Two nucleotides from one sequence
* One nucleotide from the other
  The player who cannot make a move wins.

### 🛠 Solution Overview

- Read enzyme sequences from `brain.fna` and `liver.fna`
- Simulate turns, alternating players
- Identify winning strategies for all combinations of *n* and *m*

### 💻 Implementation Details

* **Language**: Python 🐍
* **Library**: Biopython (`pip install biopython`)
* **Main Components**:

  * `liver_sequences`, `brain_sequences`: loaded sequences
  * `makeMove`: function simulating each turn

### ▶️ How to Run

1️⃣ Install Python and Biopython (`pip install biopython`)
2️⃣ Navigate to the directory containing `6_14.py`
3️⃣ Run:

```bash
python3 6_14.py
```

---

## 📚 References

**Topic 1**

* [NumPy Documentation](https://numpy.org/doc)
* [Viterbi Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Viterbi_algorithm)
* Bioinformatics course notes, University of Piraeus
* *Introduction to Bioinformatics Algorithms*, Neil C. Jones & Pavel A. Pevzner

**Topic 2**

* Bioinformatics course notes, University of Piraeus
* *Introduction to Bioinformatics Algorithms*, Neil C. Jones & Pavel A. Pevzner

**Topic 3**

* [Biopython Documentation](https://biopython.org)
