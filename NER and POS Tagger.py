import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def extract_nlp_features(text):
    doc = nlp(text)
    
    data = []
    
    for token in doc: 
        data.append({
            "Text": token.text,
            "Morpheme/Stem": token.lemma_,
            "POS": token.pos_,       
            "Tag": token.tag_,        
            "Dependency": token.dep_
        })
    
    return pd.DataFrame(data)

def extract_entities(text):
    doc = nlp(text)
    
    entities = []
    for ent in doc.ents:
        entities.append({
            "Text": ent.text,
            "Label": ent.label_,
            "Start": ent.start_char,
            "End": ent.end_char
        })
    
    return pd.DataFrame(entities)

text = "John studies in VIT Bhopal University."

pos_df = extract_nlp_features(text)
print("Token Features:\n", pos_df)

ner_df = extract_entities(text)
print("\nNamed Entities:\n", ner_df)