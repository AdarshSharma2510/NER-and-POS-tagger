# 🧠 NLP Feature Extraction using spaCy

![Python](https://img.shields.io/badge/Python-3.10-blue)
![spaCy](https://img.shields.io/badge/spaCy-NLP-green)
![Pandas](https://img.shields.io/badge/Pandas-Data--Analysis-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> 🚀 Extract linguistic features and named entities from text using spaCy

---

## 📖 Overview
This project demonstrates how to extract **token-level linguistic features** and perform **Named Entity Recognition (NER)** using the spaCy NLP library.

It processes raw text and converts it into structured data for analysis.

---

## 🚀 Features
- 🔤 Tokenization  
- 🧩 Lemmatization (base word extraction)  
- 🏷️ Part-of-Speech (POS) tagging  
- 🔍 Fine-grained grammatical tagging  
- 🔗 Dependency parsing  
- 🧠 Named Entity Recognition (NER)  

---

## 🛠️ Technologies Used
- Python 🐍  
- spaCy 🧠  
- Pandas 📊  

---

## 📦 Installation

### 1️⃣ Install dependencies
```bash
pip install spacy pandas


▶️ Usage

Run the script:

python your_script_name.py


Example Input


text = "John studies in VIT Bhopal University."


📊 Output

🔹 Token Features

Text	Lemma	POS	Tag	Dependency
John	John	PROPN	NNP	nsubj
studies	study	VERB	VBZ	ROOT
in	in	ADP	IN	prep
VIT	VIT	PROPN	NNP	compound
Bhopal	Bhopal	PROPN	NNP	compound
University	University	PROPN	NNP	pobj


🔹 Named Entities

Text	Label	Start	End
John	PERSON	...	...
VIT Bhopal University	ORG	...	...
🧠 Explanation


🔹 Token Attributes

Text → Original word
Lemma (lemma_) → Root/base form
POS (pos_) → Coarse part of speech
Tag (tag_) → Detailed grammatical tag
Dependency (dep_) → Relationship with other words


🔹 Entity Attributes

Text → Entity name
Label (label_) → Type (PERSON, ORG, GPE, etc.)
Start / End → Character positions in text