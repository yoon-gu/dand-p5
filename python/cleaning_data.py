from pandas import DataFrame, read_csv
df = read_csv('baseball_data.csv')
df = df[df.avg > 0.0]
print df.to_csv('cleand_baseball_data.csv')