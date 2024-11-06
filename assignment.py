import os
print(os.getcwd())

import pandas as pd
data = pd.read_csv("trestle_academy_dataset.csv")
print(data)

#identifying and handling missing values
missing_values = data.isnull().sum()
print(missing_values)

#standadizing text data
data['enrollment_date'] = pd.to_datetime(data['enrollment_date'], errors='coerce')
print(data.dtypes)

#normalizing text data
data['course'] = data['course'].str.title()
print(data['course'].unique())

#filtering unwanted data
filtered_data = data[(data['age'] >= 18) & (data['age'] <= 45)]
original_count = data.shape[0]
filtered_count = filtered_data.shape[0]
print("Original row count:", original_count)
print("Filtered row count:", filtered_count)

#correcting inconsistent entries
data['is_intern'] = data['is_intern'].str.title()
print(data['is_intern'].unique())