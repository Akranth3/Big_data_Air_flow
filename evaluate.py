import pandas as pd
from sklearn.metrics import r2_score

with open('params.yaml','r') as f:
    params = yaml.safe_load(f)

file_name = params['file_location']


# Load the Ground Truth Data
df_ground_truth = pd.read_csv('Ground_Truth_Data/' + file_name[0:11] + '_monthly.csv', low_memory=False)

# Load the Computed Averages Data
df_computed_avg = pd.read_csv('Computed_Averages_Data/' + file_name[0:11] + '_computed_avg.csv', low_memory=False)

print(df_ground_truth.shape, df_computed_avg.shape)


# Compute the R2 score
