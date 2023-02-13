#!/usr/bin/env python
# coding: utf-8

# In[10]:


import gensim

def preprocess_text(text):
    # Perform any preprocessing steps on the text here, such as lowercasing, tokenization, etc.
    return text.lower().split()

text_list = [
    "Text summarization is the task of generating a concise and fluent summary while preserving the most important information and overall meaning of the original text.",
    "It is a challenging problem in Natural Language Processing and has many practical applications, such as content reduction for faster information retrieval and reducing cognitive overload for the reader.",
    "There are several approaches for text summarization, including extractive methods, which select the most important sentences from the text, and abstractive methods, which generate new words and phrases that capture the meaning of the text.",
    "Word embeddings is one of the most popular techniques in NLP and has been used for various tasks such as sentiment analysis, text classification, and language translation.",
    "This technique represents words as vectors in a high-dimensional space, capturing their semantic meanings and relationships with other words."
]

# Preprocess the text
preprocessed_text_list = [preprocess_text(str(text)) for text in text_list]

# Train the word embedding model
model = gensim.models.Word2Vec(preprocessed_text_list, window=5, min_count=5, workers=4)
model.save('word_embedding_model')

