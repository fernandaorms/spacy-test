Q: What does spaCy do when you call nlp on a string of text?

```python
doc = nlp("This is a sentence.")
```

A: Tokenize the text and apply each pipeline component in order.

Response: The tokenizer turns a string of text into a Doc object. spaCy then applies every component in the pipeline on document, in order.