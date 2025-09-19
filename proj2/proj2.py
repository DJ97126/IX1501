import numpy as np

data=[56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
x_mean = np.mean(data)

numberOfResamples = 1000
result = []

#Generate new samples and add them to result
for i in range(numberOfResamples):
    sample = np.random.choice(data, size=len(data), replace=True)
    x_bootstrap_mean = np.mean(sample)
    result.append(x_bootstrap_mean-x_mean)

#Check if conditions are met
hold = 0
for i in range(len(result)):
    if (result[i] > -6 and result[i] < 4 ):
        hold+=1

probability = hold/len(result)
print(probability)