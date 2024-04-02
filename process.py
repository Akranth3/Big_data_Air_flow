import pandas as pd
import yaml

# Load the data
with open('params.yaml','r') as f:
    params = yaml.safe_load(f)

file_name = params['file_location']

df = pd.read_csv('Data/' + file_name, low_memory=False)

#Preparing the list of daily columns and extracting the data.
day_column_names = [col for col in df.columns if col[0:5] == 'Daily']
day_column_names.append('DATE')

day_data = df[day_column_names]

#converting the date to month
day_data['MONTH'] = day_data['DATE'].apply(lambda x: x[5:7])
day_data.drop('DATE', axis=1, inplace=True)

# print(day_data.columns)

for col in day_data.columns:
    print(col, day_data[col].isnull().sum()/len(day_data)*100)

# Comute the monthly data


# Save the computed monthly data
day_data.to_csv('Computed_Averages_Data/'+file_name[0:11]+'_computed_avg.csv', index=False)
