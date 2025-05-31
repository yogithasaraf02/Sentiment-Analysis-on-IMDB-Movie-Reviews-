# Sentiment count
sentiment_counts = imdb_data['sentiment'].value_counts()
print(sentiment_counts)

# Visualize sentiment distribution using a bar plot
sentiment_counts.plot(kind='bar', color=['blue', 'red'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
