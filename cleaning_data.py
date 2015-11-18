from pandas import DataFrame, read_csv, cut
# import matplotlib.pyplot as plt

df = read_csv('data/baseball_data.csv')
print df.describe()

df = df[(df.avg > 0.0) & (df.HR > 0)]
print df.describe()

print df.groupby(by='handedness').describe()

import numpy as np
df['avg_category'] = cut(df.avg, np.linspace(0.0, 0.35, 8))
print df

df.to_csv('data/cleaned_baseball.csv')