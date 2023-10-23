import logging
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk import sent_tokenize
from data import *

logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def find_sources_per_sentences(question_set: QuestionSet):
    
    result_data = {
        "question": question_set.question,
        "generative_answer": question_set.generative_answer,
        "traceback": []
    }

    logging.info(f"{'#'*10} Question: {question_set.question} {'#'*10}\n\n")
    logging.info(f"+++++++Generated_answer: {question_set.generative_answer}\n\n")

    segments = sent_tokenize(question_set.generative_answer)

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(segments + question_set.retrieved_passages,)

    # Passaggio su ogni frase della risposta generata per trovare il passaggio più simile
    passage_similarities = []
    for segment in segments:
        # Calcolo di similarità tra segmento e ogni passaggio dato al generativo
        similarities = cosine_similarity(tfidf_vectorizer.transform([segment]), tfidf_matrix[len(segments):])
        # Trova il passaggio più simile al segmento
        closest_passage_index = similarities.argmax()
        closest_passage = question_set.retrieved_passages[closest_passage_index]
        passage_similarities.append((segment, closest_passage))


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
        # print(f"Segment:\n {segment}\n\n+++++++Closest passage:\n {closest_passage}\n\n+++++++Most relevant sentence:\n {most_relevant_sentence}\n\n----\n\n")
        logging.info(f"Segment:\n {segment}\n\n+++++++Closest passage:\n {closest_passage}\n\n+++++++Most relevant sentence:\n {most_relevant_sentence}\n\n\n\n")

        result_data["traceback"].append({
            "segment": segment,
            "closest_passage": closest_passage,
            "most_relevant_sentence": most_relevant_sentence,
            "manual_score": "-"
        })
    
    with open(f"{question_set.question[:30]}.json", 'w') as json_file:
        json.dump(result_data, json_file, indent=4)

if __name__ == "__main__":
    for q in [question_set1, question_set2, question_set3, question_set4, question_set5, question_set6, question_set7]:
        find_sources_per_sentences(q)