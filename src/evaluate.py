import pandas as pd
from sklearn.metrics import r2_score
import sys
sys.path.append('../')

file_name = 'data.csv'


# Load the Ground Truth Data
df_ground_truth = pd.read_csv('Ground_Truth_Data/' + file_name[0:11] + '_monthly.csv', low_memory=False)

# Load the Computed Averages Data
df_computed_avg = pd.read_csv('Computed_Averages_Data/' + file_name[0:11] + '_computed_avg.csv', low_memory=False)

print(df_ground_truth.shape, df_computed_avg.shape)


# Compute the R2 score
r2 = r2_score(df_ground_truth['target'], df_computed_avg['target'])
results = {'R2 Score': r2}
print(results)

# Store the results in a txt file
with open('Results/results.txt', 'w') as file:
    file.write(str(results))

