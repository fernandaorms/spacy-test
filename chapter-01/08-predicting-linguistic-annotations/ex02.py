# Part 2
# Process the text and create a doc object.
# Iterate over the doc.ents and print the entity text and label_ attribute.


import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)


# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)
    print(spacy.explain(ent.label_))