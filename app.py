import streamlit as st
from tokenization import Tokenization

st.title("visual-NLP 👨🏻‍💻")
st.write("See various NLP preprocessing Tasks visually!")


corpus = st.text_area("Enter your text here!")
st.write(f"You wrote {len(corpus)} characters.")

technique = st.sidebar.selectbox("Select a Technique", ("Tokenization", "Stemming", "Lemmatization"))
subTechnique=""

def addSubTechniques(technique):
    if technique == "Tokenization":
        subTechnique = st.sidebar.selectbox("Select a Technique",("Sentence Tokenization","Word Tokenization"))

    elif technique == "Stemming":
        subTechnique = st.sidebar.selectbox("Select a Technique",(" Tokenization","Word "))

addSubTechniques(technique)

processed_text = Tokenization(corpus)
st.write(processed_text)

if technique == "Tokenization" and subTechnique == "Sentence Tokenization":
    processed_text = Tokenization(corpus)
    st.write(processed_text)
