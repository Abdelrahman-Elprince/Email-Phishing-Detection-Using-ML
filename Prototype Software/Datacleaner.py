import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import nltk

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Read the CSV file
df = pd.read_csv('new_data.csv')

# Text preprocessing: remove non-alphanumeric characters, convert to lowercase
df['combined_text'] = df['combined_text'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x.lower()))

# Tokenization, stemming, and removing stop words
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
df['combined_text'] = df['combined_text'].apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split() if word not in stop_words]))

# TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf_vectorizer.fit_transform(df['combined_text'])

# Save the modified DataFrame back to CSV
df.to_csv('new_data_processed.csv', index=False)

# Display sample of the processed DataFrame
print("Sample of processed DataFrame:")
print(df.head())
