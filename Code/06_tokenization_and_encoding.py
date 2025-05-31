# Initialize the tokenizer
max_features = 10000  # Max number of words to consider
max_length = 150      # Maximum length of each review (number of words)

tokenizer = Tokenizer(num_words=max_features, lower=True, split=' ')
tokenizer.fit_on_texts(imdb_data['cleaned_review'])

# Convert the reviews to sequences of integers
X = tokenizer.texts_to_sequences(imdb_data['cleaned_review'])

# Pad sequences to ensure all have the same length
X = pad_sequences(X, padding='post', maxlen=max_length)

# Convert the 'sentiment' labels to numeric values (positive=1, negative=0)
y = imdb_data['sentiment'].map({'positive': 1, 'negative': 0}).values
