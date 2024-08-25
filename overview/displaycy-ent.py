import spacy
from spacy import displacy

# Carregar o modelo spaCy
nlp = spacy.load("en_core_web_sm")


# Processar os textos
doc1 = nlp("Apple is looking at buying U.K. startup for $1 billion")
doc2 = nlp("Microsoft Corporation is an American multinational technology company.")


# Definir as cores para os tipos de entidades
colors = {"ORG": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}

options = {"colors": colors}

# displacy.serve(doc, style="dep", host="127.0.0.1")
displacy.serve([doc1, doc2], style="ent", options=options, host="127.0.0.1")
# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)