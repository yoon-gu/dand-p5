from pandas import DataFrame, read_csv, cut
import numpy as np

df = read_csv('data/baseball_data.csv')
df = df[(df.avg > 0.0) & (df.HR > 0)]

## Split to 5 intervals using pandas.cut function
df['avg_category'] = cut(df.avg, 
						bins = np.linspace(0.1, 0.35, 6), 
						right=False)

## Except 'height', 'weight', 'avg', grouping df by 'avg_category', 'handedness'
## And add all sub-group's entries
avg_handedness_count_df = df.drop(['height', 'weight', 'avg'], axis=1).groupby(by=['avg_category', 'handedness']).sum().reset_index()
avg_partical_count  = df.drop(['height', 'weight', 'name', 'avg', 'handedness'], axis=1).groupby(by=['avg_category']).sum()

## Except 'height', 'weight', 'avg', grouping df by 'avg_category'
## And add all sub-group's entries 
## This is for compute HR ratio
avg_count_df = avg_partical_count.add_prefix('total_').reset_index()
final_df = avg_handedness_count_df.merge(avg_count_df, on='avg_category')
final_df['HR_Percent'] = final_df.HR / final_df.total_HR * 100.

## Grouping and merge to get mean of home runs for each group
mean_hr_group = df.drop(['height', 'weight', 'avg'], axis=1).groupby(by=['avg_category', 'handedness']).mean().add_prefix('mean_').reset_index()
final_df = final_df.merge(mean_hr_group, on=['avg_category', 'handedness'])

## Save dataframe to .csv file
final_df.to_csv('data/cleaned_baseball.csv')