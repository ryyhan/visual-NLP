import streamlit as st
from tokenization import sentenceTokenization, wordTokenization
from stemming import porterStemming

st.title("visual-NLP 👨🏻‍💻")
st.write("See various NLP preprocessing Tasks visually!")


corpus = st.text_area("Enter your text here!")
st.write(f"You wrote {len(corpus)} characters.")


techniques = "NA"
subTechniques = "NA"


def addTechniques() -> None:
    global techniques
    techniques = st.sidebar.selectbox("Select a Technique", ("Tokenization", "Stemming", "Lemmatization","Stop words removal", "Parts of Speech (POS) Tagging", "Named Entity Recognition"))

def addSubTechniques(techniques) -> None:
    global subTechniques
    if techniques == "Tokenization":
        subTechniques = st.sidebar.selectbox("Select a Technique",("Sentence Tokenization","Word Tokenization"))

    elif techniques == "Stemming":
        subTechniques = st.sidebar.selectbox("Select a Sub-Technique",("Porter Stemmer","Regexp Stemmer", "Snowball Stemmer"))

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
        processed_text = porterStemming(corpus)
        st.write(processed_text)

    elif techniques == "Stemming" and subTechniques == "Snowball Stemmer":
        st.write(explanation(subTechniques))
        st.success("Result:")
        processed_text = porterStemming(corpus)
        st.write(processed_text)

    
