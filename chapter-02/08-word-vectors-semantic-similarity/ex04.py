import spacy

# Load a larger pipeline with vectors
nlp = spacy.load("en_core_web_md")

doc1 = nlp("I like cats")
doc2 = nlp("I hate cats")

print(doc1.similarity(doc2))