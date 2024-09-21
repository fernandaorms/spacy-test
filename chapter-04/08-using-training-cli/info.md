* Call the train command with the file exercises/en/config_gadget.cfg.
* Save the trained pipeline to a directory output.
* Pass in the exercises/en/train_gadget.spacy and exercises/en/dev_gadget.spacy paths.

```python
python -m spacy train ./config_gadget.cfg --output ./output --paths.train ./train_gadget.spacy --paths.dev ./dev_gadget.spacy
```