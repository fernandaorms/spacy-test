# Import the Matcher from spacy.matcher.
# Initialize it with the nlp object’s shared vocab.
# Create a pattern that matches the "TEXT" values of two tokens: "iPhone" and "X".
# Use the matcher.add method to add the pattern to the matcher.
# Call the matcher on the doc and store the result in the variable matches.
# Iterate over the matches and get the matched span from the start to the end index.


import spacy

# Import the Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialize the Matcher with the shared vocabulary
matcher = Matcher(nlp.vocab)

# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Add the pattern to the matcher
matcher.add("IPHONE_X_PATTERN", [pattern])

# Use the matcher on the doc
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])