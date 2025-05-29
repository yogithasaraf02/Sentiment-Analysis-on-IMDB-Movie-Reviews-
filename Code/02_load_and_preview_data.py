from google.colab import files
import pandas as pd

# Upload the file
uploaded = files.upload()

# Load the dataset
imdb_data = pd.read_csv('IMDB Dataset.csv')  # Make sure the file name matches the uploaded file

# Display basic info about the dataset
print(imdb_data.shape)         # Show number of rows and columns
print(imdb_data.head(10))      # Display the first 10 rows of the dataset
