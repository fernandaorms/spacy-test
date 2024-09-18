import spacy

nlp = spacy.blank("en")

nlp.vocab.strings.add("coffee")
coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]

print(coffee_hash)
print(coffee_string)

# Raises an error if we haven't seen the string before
# string = nlp.vocab.strings[3197928453018144401]
# print(string)