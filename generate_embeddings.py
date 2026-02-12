import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

with open("documents.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(documents).toarray()
np.save("embeddings.npy", embeddings)
print("Document embeddings generated successfully!")