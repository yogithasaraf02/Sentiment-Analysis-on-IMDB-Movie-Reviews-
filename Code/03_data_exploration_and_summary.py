# 1. Overview of the dataset: Summary statistics
print(imdb_data.describe())  # Will show summary statistics for numeric columns, if any.

# 2. Check for missing values and data types
print(imdb_data.info())

# 3. Check the distribution of sentiments (positive vs. negative reviews)
print(imdb_data['sentiment'].value_counts())

# 4. Check for any missing values in the dataset
print(imdb_data.isnull().sum())
