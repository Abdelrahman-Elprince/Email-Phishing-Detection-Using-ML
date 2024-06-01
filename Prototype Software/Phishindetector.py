import pandas as pd
import pickle

# Load the pre-trained model
model_loader = pickle.load(open('D:/THESIS PROJECT/Multinomial_Naive_Bayes_classifier.pkl', 'rb'))

# Load the new data from the CSV file
new_data = pd.read_csv('new_data_processed.csv')

# Assuming 'combined_text' is the name of the column containing raw text data
# Assuming 'label' is the name of the column where you want to store the predicted labels

# Load the TF-IDF vectorizer used during training
tfidf_vectorizer = pickle.load(open('D:/THESIS PROJECT/tfidf_vectorizer.pkl', 'rb'))

# Vectorize the text data using the loaded TF-IDF vectorizer
X_new = tfidf_vectorizer.transform(new_data['combined_text'])

# Predict labels using the loaded model
predicted_labels = model_loader.predict(X_new)

# Add the predicted labels to the DataFrame
new_data['label'] = predicted_labels

# Save the updated DataFrame to a new CSV file or perform any other desired actions
new_data.to_csv('predicted_new_data.csv', index=False)
