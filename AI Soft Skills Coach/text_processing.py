from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

import streamlit as st

@st.cache_resource
def load_model():
    return SentenceTransformer('paraphrase-MiniLM-L6-v2')

def evaluate_response(user_response, ideal_answers):
    """
    Compares the user's response with ideal answers and returns similarity scores.
    """
    model = load_model()
    user_embedding = model.encode([user_response])
    ideal_embeddings = model.encode(ideal_answers)
    
    similarity_scores = cosine_similarity(user_embedding, ideal_embeddings).flatten()
    
    return similarity_scores


def evaluate_clarity(text):
    """
    A simple clarity evaluator based on the number of words and sentence complexity.
    Returns a score between 0 and 1, where 1 is perfectly clear.
    """
    words = text.split()
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    if sentence_count == 0:
        sentence_count = 1  # Prevent division by zero
    
    avg_sentence_length = len(words) / sentence_count

    # Simplicity heuristic: the longer the average sentence, the lower the clarity score
    clarity_score = 1 / (1 + avg_sentence_length)
    
    return clarity_score


def analyze_text(user_response, ideal_answers):
    """
    Analyzes the user's response for clarity, relevance, and structure.
    Returns feedback based on text metrics and similarity scores.
    """

    feedback = []
    
    clarity_score=1
    
    # Check clarity (basic metric: word count and complexity)
    clarity_score = evaluate_clarity(user_response)
    if clarity_score < 0.5:
            feedback.append("Your response could be clearer. Try to simplify your sentences.")
    
    # Evaluate relevance (similarity score with ideal answers)
    similarity_scores = evaluate_response(user_response, ideal_answers)
    
    if max(similarity_scores) < 0.7:
        feedback.append("Your response is not very relevant to the question. Try to align it more closely with the main question.")
    
    if len(user_response.split()) < 20:
        feedback.append("Your answer is short. Try to elaborate more on your experience or knowledge.")

    return {
        'clarity': clarity_score,
        'relevance': max(similarity_scores),
        'feedback': feedback
    }
