import os
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')
stemmer = SnowballStemmer('english')
stop_words = set(stopwords.words('english'))

# Function to load JSON files from a directory
def load_json_files(directory):
    json_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                json_files.append(json_data)
    return json_files

# Load JSON documents from the 'patent_jsons/' directory
documents = load_json_files('app\patent_jsons/')

# Function to perform semantic search using TF-IDF and cosine similarity
# Function to perform semantic search using TF-IDF and cosine similarity
def semantic_search(query):
    # Preprocess the query: tokenize, remove stop words, and stem
    query_tokens = word_tokenize(query)
    query_tokens = [stemmer.stem(token) for token in query_tokens if token not in stop_words]
    query_text = ' '.join(query_tokens)

    # Create a list of document texts
    document_texts = [' '.join(word_tokenize(doc.get('content', ''))) for doc in documents]

    # Check if all documents contain only stop words
    if all(not text for text in document_texts):
        return []  # No meaningful content in documents

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([query_text] + document_texts)

    # Calculate cosine similarity between the query and documents
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Handle division by zero error and empty documents
    relevant_documents = []
    for index, similarity in enumerate(cosine_similarities):
        if not similarity:
            continue  # Skip documents with zero similarity
        if similarity > relevance_threshold:
            relevant_documents.append(documents[index])

    return relevant_documents

