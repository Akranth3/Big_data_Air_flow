import pandas as pd
import pickle
import sys
sys.path.append('../')

# Load the data


file_name = 'data.csv'

df = pd.read_csv('Data/' + file_name, low_memory=False)

#Preparing the list of daily columns and extracting the data.
month_column_names = pickle.load(open('Ground_Truth_Data/'+'monthly_columns.pkl', 'rb'))
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
day_data.to_csv('Computed_Averages_Data/'+'computed_avg.csv', index=False)
