# Malayalam-English Cross-Lingual Semantic Knowledge Graph & Text Analytics Pipeline

Developed as part of academic preparation for the **Erasmus Mundus Joint Master in European Linguistic Data Science (EMLDS)**.

## 📌 Overview
This project presents an end-to-end NLP and Semantic Web analytics tool designed to process multi-lingual text corpora, extract grammatical/linguistic features, extract Subject-Predicate-Object semantic triples, and visualize interactive **Knowledge Graphs** aligned with **Linguistic Linked Data (LLD)** principles.

## ✨ Key Features
- **Linguistic Feature Extraction:** Tokenization, Lemmatization, and POS Tagging using SpaCy.
- **Named Entity Recognition (NER):** Automatic classification of proper nouns and entities.
- **Triple Extraction Engine:** Parses dependency trees to formulate `(Subject, Predicate, Object)` semantic relations.
- **Interactive Knowledge Graph:** Generates dynamic graph visualizations via NetworkX and PyVis.
- **Sentiment & Subjectivity Metrics:** TextBlob integration for polarity evaluation.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **NLP Libraries:** SpaCy, NLTK, TextBlob
- **Graph & Visualization:** NetworkX, PyVis, Streamlit