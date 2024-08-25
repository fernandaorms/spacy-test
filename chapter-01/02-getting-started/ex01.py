# Part 1: English
# Use spacy.blank to create a blank English ("en") nlp object.
# Create a doc and print its text.


# Import spaCy
import spacy

# Create the English nlp object
nlp = spacy.blank("en")

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)