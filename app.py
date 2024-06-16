import streamlit as st
from tokenization import sentenceTokenization, wordTokenization
from stemming import porterStemming, regexpStemmer, snowballStemmer
from stopwordsremoval import stopWordsRemoval
from lemmatization import wordnetLemmatizer
from ner import namedEntityRecognition
from pos import posTagging

st.title("visual-NLP 👨🏻‍💻")
st.write("See various NLP preprocessing Tasks visually!")


corpus = st.text_area("Enter your text here!")
st.write(f"You wrote {len(corpus)} characters.")


techniques = "NA"
subTechniques = "NA"


def addTechniques() -> None:
    global techniques
    techniques = st.sidebar.selectbox("Select a Technique", ("Tokenization", "Stemming", "Lemmatization","Stop words removal", "Parts of Speech (POS) Tagging", "Named Entity Recognition (NER)"))

def addSubTechniques(techniques) -> None:
    global subTechniques
    if techniques == "Tokenization":
        subTechniques = st.sidebar.selectbox("Select a Technique",("Sentence Tokenization","Word Tokenization"))

    elif techniques == "Stemming":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique",("Porter Stemmer","Regexp Stemmer", "Snowball Stemmer"))

    elif techniques == "Lemmatization":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique",("Wordnet Lemmatizer",))

    elif techniques == "Stop words removal":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique",("English",))

    elif techniques == "Parts of Speech (POS) Tagging":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique",("using NLTK",))

    elif techniques == "Named Entity Recognition (NER)":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique",("MaxEnt NE Chunker",))

def explanation(subTechniques) -> str:
    if subTechniques == "Sentence Tokenization":
        return "Sentence tokenization in NLP is the process of breaking down a large piece of text into individual sentences. It's like cutting a long rope into smaller strings. It helps NLP models identify sentences, improve accuracy, and streamline processing. It's done by splitting on punctuation, using whitespace, and regular expressions to separate sentences."

    elif subTechniques == "Word Tokenization":
        return "Word tokenization in NLP is the process of breaking down text into individual words or tokens. It helps NLP models understand text better by identifying individual words, improving accuracy, and streamlining processing. Tokenization is done by splitting on whitespace, punctuation, and regular expressions to separate words."

    elif subTechniques == "Porter Stemmer":
        return "Porter Stemming is a algorithm used in NLP to reduce words to their base or root form. It's a simple and fast method to reduce words to their stem, removing prefixes and suffixes. For example, 'running' becomes 'run'. Porter Stemming is widely used in text processing, information retrieval, and text classification tasks."

    elif subTechniques == "Regexp Stemmer":
        return "Regexp Stemming is a method used in NLP to reduce words to their base or root form. It uses regular expressions to identify and remove prefixes and suffixes, resulting in a stemmed word. For example, 'running' becomes 'run'. Regexp Stemming is more accurate than Porter Stemming, but slower and more complex. It's used in text processing, information retrieval, and text classification tasks."

    elif subTechniques == "Snowball Stemmer":
        return "Snowball Stemming is a stemming algorithm used in NLP to reduce words to their base or root form. It's a more advanced algorithm than Porter Stemming, with better accuracy and handling of irregularities. Snowball Stemming is used in many NLP applications, including text processing, information retrieval, and text classification."

    elif subTechniques == "Wordnet Lemmatizer":
        return "WordNet Lemmatization is a process in NLP that uses a lexical database called WordNet to map words to their base or dictionary form, called the lemma. It's a more accurate and precise method than stemming, as it takes into account the word's part of speech and context. WordNet Lemmatization is used in many NLP applications, including text processing, information retrieval, and text classification."

    elif subTechniques == "English":
        return "Stop words removal is a process in NLP that involves removing common words like 'the', 'and', 'a', etc. from a text dataset. These words are called stop words because they don't carry much meaning in the context of the text. Removing stop words helps to reduce noise, improve search results, and enhance text analysis."

    elif subTechniques == "using NLTK":
        return "Parts of Speech (POS) tagging is a process in NLP that identifies the grammatical category of each word in a sentence, such as noun, verb, adjective, adverb, etc. POS tagging helps computers understand the meaning and context of text by identifying the part of speech of each word."

    elif subTechniques == "MaxEnt NE Chunker":
        return "Named Entity Recognition (NER) is a process in NLP that identifies and categorizes named entities in unstructured text into predefined categories such as person, organization, location, date, time, etc. NER helps computers understand the meaning and context of text by identifying specific entities and their types."


addTechniques()
addSubTechniques(techniques)


if st.button("start", type="primary"):
    if techniques == "Tokenization" and subTechniques == "Sentence Tokenization":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = sentenceTokenization(corpus)
        st.write(processed_text)

    elif techniques == "Tokenization" and subTechniques == "Word Tokenization":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = wordTokenization(corpus)
        st.write(processed_text)

    elif techniques == "Stemming" and subTechniques == "Porter Stemmer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = porterStemming(corpus)
        st.write(processed_text)

    elif techniques == "Stemming" and subTechniques == "Regexp Stemmer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = regexpStemmer(corpus)
        st.write(processed_text)

    elif techniques == "Stemming" and subTechniques == "Snowball Stemmer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = snowballStemmer(corpus)
        st.write(processed_text)

    elif techniques == "Lemmatization" and subTechniques == "Wordnet Lemmatizer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = wordnetLemmatizer(corpus)
        st.write(processed_text)

    elif techniques == "Stop words removal" and subTechniques == "English":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = stopWordsRemoval(corpus)
        st.write(processed_text)

    elif techniques == "Parts of Speech (POS) Tagging" and subTechniques == "using NLTK":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = posTagging(corpus)
        st.write(processed_text)

    elif techniques == "Named Entity Recognition (NER)" and subTechniques == "MaxEnt NE Chunker":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = namedEntityRecognition(corpus)
        st.write(processed_text)
