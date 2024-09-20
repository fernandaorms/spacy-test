import spacy

from spacy.tokens import Token

nlp = spacy.load("en_core_web_sm")

# Set extension on the Token with default value
Token.set_extension("is_color", default=False)

doc = nlp("The sky is blue.")

# Overwrite extension attribute value
doc[3]._.is_color = True

for token in doc:
    print(f'Text: {token.text} - Is Color: {token._.is_color}')