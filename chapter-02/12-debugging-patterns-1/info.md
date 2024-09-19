Q: Why does this pattern not match the tokens “Silicon Valley” in the doc?

```python
pattern = [{"LOWER": "silicon"}, {"TEXT": " "}, {"LOWER": "valley"}]
```

```python
doc = nlp("Can Silicon Valley workers rein in big tech from within?")
```

A: The tokenizer doesn’t create tokens for single spaces, so there’s no token with the value " " in between.

Response: The tokenizer already takes care of splitting off whitespace and each dictionary in the pattern describes one token.