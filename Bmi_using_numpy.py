import numpy as np
height = [1.68,1.56,1.73,1.93]
weight = [55,65.2,59.2,70.6]
np_height = np.array(height)
np_weight = np.array(weight)


bmi = np_weight / (np_height * np_height)

print(bmi)
