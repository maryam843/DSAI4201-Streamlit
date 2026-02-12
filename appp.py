import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("documents.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

vectorizer = TfidfVectorizer(lowercase=True)
embeddings = vectorizer.fit_transform(documents).toarray()

def retrieve_top_k(query_embedding, embeddings, k=10):
    similarities = cosine_similarity(query_embedding.reshape(1, -1), embeddings)[0]
    top_k_indices = similarities.argsort()[-k:][::-1]
    return [(documents[i], similarities[i]) for i in top_k_indices if similarities[i] > 0]

st.title("Information Retrieval using Document Embeddings")
query = st.text_input("Enter your query:")

def get_query_embedding(query):
    return vectorizer.transform([query]).toarray()[0]

if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a query first!")
    else:
        query_embedding = get_query_embedding(query)
        results = retrieve_top_k(query_embedding, embeddings)
        
        if len(results) == 0:
            st.info("No relevant documents found for your query.")
        else:
            st.write("### Top Relevant Documents:")
            for doc, score in results:
                st.write(f"- **{doc.strip()}** (Score: {score:.4f})")
