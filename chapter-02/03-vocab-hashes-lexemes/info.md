Q: Why does this code throw an error?

```python
import spacy

# Create an English and German nlp object
nlp = spacy.blank("en")
nlp_de = spacy.blank("de")

# Get the ID for the string 'Bowie'
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# Look up the ID for "Bowie" in the vocab
print(nlp_de.vocab.strings[bowie_id])
```

A: he string "Bowie" isn’t in the German vocab, so the hash can’t be resolved in the string store.

Response: Hashes can’t be reversed. To prevent this problem, add the word to the new vocab by processing a text or looking up the string, or use the same vocab to resolve the hash back to a string.