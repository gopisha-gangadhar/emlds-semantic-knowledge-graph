import spacy
import nltk
from textblob import TextBlob
import pandas as pd

# Download NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

try:
    nlp = spacy.load("en_core_web_sm")
except:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

class LinguisticPipeline:
    def __init__(self):
        self.nlp = nlp

    def process_text(self, text):
        doc = self.nlp(text)
        
        # 1. Linguistic Features (POS Tagging & Lemmatization)
        tokens_info = []
        for token in doc:
            if not token.is_stop and not token.is_punct:
                tokens_info.append({
                    "Token": token.text,
                    "Lemma": token.lemma_,
                    "POS": token.pos_,
                    "Tag": token.tag_
                })
        
        # 2. Named Entity Recognition (NER)
        entities = [{"Text": ent.text, "Label": ent.label_} for ent in doc.ents]
        
        # 3. Sentiment Analysis
        blob = TextBlob(text)
        sentiment = {
            "Polarity": round(blob.sentiment.polarity, 2),
            "Subjectivity": round(blob.sentiment.subjectivity, 2)
        }
        
        # 4. Extract Entity Relationships for Knowledge Graph
        triples = []
        for sent in doc.sents:
            subj, verb, obj = None, None, None
            for token in sent:
                if "subj" in token.dep_:
                    subj = token.text
                elif "verb" in token.pos_.lower() or token.pos_ == "VERB":
                    verb = token.lemma_
                elif "obj" in token.dep_:
                    obj = token.text
            if subj and verb and obj:
                triples.append((subj, verb, obj))
                
        return pd.DataFrame(tokens_info), pd.DataFrame(entities), sentiment, triples