# Step 1
# Use spacy.blank to create the English nlp object.
# Process the text and instantiate a Doc object in the variable doc.
# Select the first token of the Doc and print its text.


# Import spaCy and create the English nlp object
import spacy

nlp = spacy.blank("en")

# Process the text
doc = nlp("I like tree kangaroos and narwhals.")

# Select the first token
first_token = doc[0]

# Print the first token's text
print(first_token.text)