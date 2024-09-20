### Anatomy of a component (1)

* Function that takes a doc, modifies it and returns it
* Registered using the Language.component decorator
* Can be added using the nlp.add_pipe method

```python
from spacy.language import Language

@Language.component("custom_component")
def custom_component_function(doc):
    # Do something to the doc here
    return doc

nlp.add_pipe("custom_component")
```


### Anatomy of a component (2)

| Argument | Description                | Example                                         |
|----------|----------------------------|-------------------------------------------------|
| `last`   | If True, add last           | `nlp.add_pipe("component", last=True)`           |
| `first`  | If True, add first          | `nlp.add_pipe("component", first=True)`          |
| `before` | Add before component        | `nlp.add_pipe("component", before="ner")`        |
| `after`  | Add after component         | `nlp.add_pipe("component", after="tagger")`      |
