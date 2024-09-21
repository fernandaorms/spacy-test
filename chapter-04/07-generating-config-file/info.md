### Part 1

* Use spaCy’s init config command to auto-generate a config for an English pipeline.
* Save the config to a file config.cfg.
* Use the --pipeline argument to specify one pipeline component, ner.

```python
python -m spacy init config ./config.cfg --lang en --pipeline ner
```

### Part 2

Let’s take a look at the config spaCy just generated! You can run the command below to print the config to the terminal and inspect it.

```python
cat ./config.cfg
```