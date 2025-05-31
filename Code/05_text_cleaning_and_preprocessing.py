# Text cleaning function
def clean_text(text):
    text = re.sub(r'<.*?>', ' ', text)  # Remove HTML tags
    text = re.sub(r'https?://\S+', ' ', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # Remove non-alphabetical characters
    text = text.lower()  # Convert to lowercase
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])  # Remove stopwords
    return text

# Apply the text cleaning function to the 'review' column
imdb_data['cleaned_review'] = imdb_data['review'].apply(clean_text)
