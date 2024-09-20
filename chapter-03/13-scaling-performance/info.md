### Processing large volumes of text

* Use nlp.pipe method
* Processes texts as a stream, yields Doc objects
* Much faster than calling nlp on each text

**BAD:**
```python
docs = [nlp(text) for text in LOTS_OF_TEXTS]
```

**GOOD:**
```python
docs = list(nlp.pipe(LOTS_OF_TEXTS))
```



### Passing in context (1)

* Setting as_tuples=True on nlp.pipe lets you pass in (text, context) tuples
* Yields (doc, context) tuples
* Useful for associating metadata with the doc



### Passing in context (2)

Check code.


### Using only the tokenizer (2)

* Use nlp.make_doc to turn a text into a Doc object

**BAD:**
```python
doc = nlp("Hello world")
```

**GOOD:**
```python
doc = nlp.make_doc("Hello world!")
```


### Disabling pipeline components

* Use nlp.select_pipes to temporarily disable one or more pipes

```python
# Disable tagger and parser
with nlp.select_pipes(disable=["tagger", "parser"]):
    # Process the text and print the entities
    doc = nlp(text)
    print(doc.ents)
```

* Restores them after the with block
* Only runs the remaining components