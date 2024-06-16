import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize

def sentenceTokenization(corpus):
    processed_text = sent_tokenize(corpus)
    return processed_text

def wordTokenization(corpus):
    processed_text = word_tokenize(corpus)
    return processed_text