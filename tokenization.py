import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def Tokenization(corpus):
    processed_text = sent_tokenize(corpus)
    return processed_text