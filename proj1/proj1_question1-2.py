import numpy

# Define probability for different dice.
# Each entery in the list shows the probability of rolling that face.
d4 = [1/4, 1/4, 1/4, 1/4]
d6 = [1/6,1/6,1/6,1/6,1/6,1/6]
d8 = [1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8]
d12 =[1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12,1/12]
d20 = [1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20]

# Put all dice distrubutions in a list.
dices = [d4,d6,d8,d12,d20]

# Convolution combines two independent distributions.
# After each step, update distribution to include the next die.
for i in range(4):
    dNew = numpy.convolve(dices[i], dices[i+1])
    dices[i+1] = dNew

# Print combined probability.
print(dNew)

# Calculate probability of winning.
# total is <= 6 or >= 46
winning = 0
for i in range(6):
    winning = winning + dNew[i]
for i in range(6):
    winning = winning + dNew[i+40]

print(winning)