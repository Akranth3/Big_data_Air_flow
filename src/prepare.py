import pandas as pd
import pickle
import sys


sys.path.append('../')

# Load the data
file_name = 'data.csv'

df = pd.read_csv('Data/' + file_name, low_memory=False)

#Extract the monthly data
monthly_column_names = [col for col in df.columns if col[0:7] == 'Monthly']
monthly_column_names.append('DATE')

monthly_data = df[monthly_column_names]
monthly_data['MONTH'] = monthly_data['DATE'].apply(lambda x: x[5:7])

# Drop the date
monthly_data.drop('DATE', axis=1, inplace=True)

# Handle the missing data, since we are calculating mean so replacing the 
# missing values by mean is the best way to handle missing data
monthly_data.dropna(axis=1, how='all', inplace=True)
monthly_data.fillna(monthly_data.mean(), inplace=True)

monthly_data['Dummy'] = 1.0

# save the list of column names
pickle.dump(monthly_data.columns, open('Ground_Truth_Data/'+'monthly_columns.pkl', 'wb'))


# Save the monthly data
monthly_data.to_csv('Ground_Truth_Data/'+'monthly.csv', index=False)

