## Generating Random Numbers 
# For simulations and examing hipotetycal scenarios
# 


import pandas as pd
import numpy as np
import math # For mathematical operations
import random # For generating random numbers
import statsmodels # For descriptive statistics, regression and time series 
import pandas_datareader # For downloading stock data
import matplotlib.pyplot as plt # For data visualization
import seaborn as sns # For statistical visualization
import scipy # For scientific computing


# Arrays: All the data inside must be the same datatype

a = np.array([[0,2,3],[1,4,6]])
a.shape


# random to run simulations, beautiful for examing hipotetical scenarios. Sometimes, the real data is not available or not enough.

prob = np.random.rand(1)
print(prob)

number = random.randint(1,10)
print(number)

np.random.randint(1,10,(4,6))

