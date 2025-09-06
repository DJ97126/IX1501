from numpy import random

# Define number of trials.
numberOfTrials = 100000
winningTrials = 0

# Randomize value for each die.
for i in range(numberOfTrials):
    d4 = random.randint(1,5)
    d6 = random.randint(1,7)
    d8 = random.randint(1,9)
    d12 = random.randint(1,13)
    d20 = random.randint(1,21)

    # Sum result 
    result = d4 + d6 + d8 + d12 + d20
    if(result <= 10 or result >= 45):
        winningTrials = winningTrials + 1

# Calculate the probability of winning.
probability = winningTrials / numberOfTrials

print(f"Probability of winning the game: {probability}")