import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from pipeline import LinguisticPipeline
from graph_builder import create_knowledge_graph

st.set_page_config(page_title="Linguistic Knowledge Graph Explorer", page_icon="🌐", layout="wide")

st.title("🌐 Cross-Lingual Linguistic Data Science & Knowledge Graph Explorer")
st.markdown("""
*Developed for research alignment with **Erasmus Mundus EMLDS**. Demonstrates Natural Language Processing, Lemmatization, Entity Relations, and Semantic Knowledge Graphs.*
""")

pipeline = LinguisticPipeline()

# Input area
default_text = "Natural Language Processing enables computers to understand human language. EMLDS integrates computational linguistics and data science to build semantic knowledge structures."
user_text = st.text_area("Enter Text / Corpus for Linguistic Analysis:", default_text, height=100)

if st.button("Run Linguistic Pipeline & Build Graph"):
    tokens_df, entities_df, sentiment, triples = pipeline.process_text(user_text)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Linguistic Features & POS Analysis")
        st.dataframe(tokens_df, use_container_width=True)
        
        st.subheader("🏷️ Named Entities (NER)")
        if not entities_df.empty:
            st.dataframe(entities_df, use_container_width=True)
        else:
            st.info("No explicit Named Entities found.")
            
        st.subheader("🎭 Sentiment Metrics")
        st.json(sentiment)

    with col2:
        st.subheader("🕸️ Semantic Knowledge Graph (Subject-Predicate-Object)")
        if triples:
            html_file = create_knowledge_graph(triples)
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            components.html(html_content, height=470)
        else:
            st.warning("No explicit Subject-Verb-Object triples extracted to construct a graph. Try adding more complex sentences.")