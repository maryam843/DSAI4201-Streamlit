# DSAI4201-Streamlit

This is an Information Retrieval (IR) app built using Streamlit and TF-IDF document embeddings.  
It allows users to enter a query and retrieve the top relevant documents from a small AI-related dataset.

## Features

- Enter any query related to AI, Machine Learning, or Robotics.
- Retrieves top relevant sentences from the dataset using cosine similarity.
- Only shows documents with a non-zero relevance score.
- Case-insensitive search.

## Files in this Repository

- appp.py → Main Streamlit application.  
- documents.txt → Dataset of AI-related sentences.  
- requirements.txt → Python dependencies required to run the app.  
- results.pdf → Screenshots showing the app working with example queries.
- 
## How to Use

1. Open the app: https://dsai4201-app-m74zuvz9zhepes5kz48pus.streamlit.app/
2. Enter a query in the text box.  
3. Click Search to see the top relevant documents.  

### Example Queries to enter

- Artificial Intelligence  
- Machine Learning  
- AI in healthcare  
- Robotics  
- Natural Language Processing  

## Deployment

The app is deployed on Streamlit Cloud. It automatically installs dependencies from requirements.txt and runs directly from appp.py
