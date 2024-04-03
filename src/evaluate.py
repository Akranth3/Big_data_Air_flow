import pandas as pd
from sklearn.metrics import r2_score
import sys
sys.path.append('../')

file_name = 'data.csv'


# Load the Ground Truth Data
df_ground_truth = pd.read_csv('Ground_Truth_Data/' + 'monthly.csv', low_memory=False)

# Load the Computed Averages Data
df_computed_avg = pd.read_csv('Computed_Averages_Data/' + 'computed_avg.csv', low_memory=False)

print(df_ground_truth.shape, df_computed_avg.shape)
print(df_computed_avg.columns, df_ground_truth.columns)

# Compute the R2 score
results = {}
for i in df_computed_avg.columns:
    if i[-6:] in df_ground_truth.columns:
        r2 = r2_score(df_ground_truth[i[-6:]], df_computed_avg[i])
        results[i] = [r2, r2>0.9]
print(results)

# Store the results in a txt file
with open('Results/results.txt', 'w') as file:
    file.write(str(results))

