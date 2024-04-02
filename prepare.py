import pandas as pd
import yaml
# Load the data
with open('params.yaml','r') as f:
    params = yaml.safe_load(f)

file_name = params['file_location']

df = pd.read_csv('Data/' + file_name, low_memory=False)

#Extract the monthly data
monthly_column_names = [col for col in df.columns if col[0:7] == 'Monthly']
monthly_data = df[monthly_column_names]


# Print the number of missing values in the monthly data
print("Number of missing values in the monthly data: ", monthly_data.isnull().sum().sum())
for col in monthly_data.columns:
    print(col, monthly_data[col].isnull().sum()/len(monthly_data)*100)

# Handle the missing data


# Save the monthly data
monthly_data.to_csv('Ground_Truth_Data/'+file_name[0:11]+'_monthly.csv', index=False)

