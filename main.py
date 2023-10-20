from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk import sent_tokenize
from data import retrieved_passages


generated_answer = "This site manufactures satellites, satellite components as well as sensors and antenna systems for satellites. Primary customers are the U.S. Government include the Department of Defense and NASA, as well as private industry who work with space and earth sciences."
segments = sent_tokenize(generated_answer)


tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(segments + retrieved_passages)

# Passaggio su ogni frase della risposta generata per trovare il passaggio più simile
passage_similarities = []
for segment in segments:
    # Calcolo di similarità tra segmento e ogni passaggio dato al generativo
    similarities = cosine_similarity(tfidf_vectorizer.transform([segment]), tfidf_matrix[len(segments):])
    # Trova il passaggio più simile al segmento
    closest_passage_index = similarities.argmax()
    closest_passage = retrieved_passages[closest_passage_index]
    passage_similarities.append((segment, closest_passage))
    # print(f"Segment: {segment}\nClosest passage: {closest_passage}")

#Stessa cosa di prima ma sulle singole frasi del passaggio più vicino invece che su tutti i passaggi
most_relevant_sentences = []
for segment, closest_passage in passage_similarities:
    # Tokenizza il passaggio più vicino in frasi
    sentences = sent_tokenize(closest_passage)
    sentence_similarities = cosine_similarity(tfidf_vectorizer.transform([segment]), tfidf_vectorizer.transform(sentences))
    # Trova la frase con la similarità più vicina al segmento di risposta generata
    most_relevant_sentence_index = sentence_similarities.argmax()
    most_relevant_sentence = sentences[most_relevant_sentence_index]
    most_relevant_sentences.append((segment, closest_passage, most_relevant_sentence))
    print(f"Segment:\n {segment}\n\n+++++++Closest passage:\n {closest_passage}\n\n+++++++Most relevant sentence:\n {most_relevant_sentence}\n\n----\n\n")

