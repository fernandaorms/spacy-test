### The training config (1)


* single source of truth for all settings
* typically called config.cfg
* defines how to initialize the nlp object
* includes all settings about the pipeline components and their model implementations
* configures the training process and hyperparameters
* makes your training more reproducible



### The training config (2)
```python
[nlp]
lang = "en"
pipeline = ["tok2vec", "ner"]
batch_size = 1000

[nlp.tokenizer]
@tokenizers = "spacy.Tokenizer.v1"

[components]

[components.ner]
factory = "ner"

[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
hidden_width = 64
# And so on...
```



### Generating a config

* spaCy can auto-generate a default config file for you
* interactive [quickstart widget](https://spacy.io/usage/training#quickstart) in the docs
* [init config](https://spacy.io/api/cli#init-config) command on the CLI

```python
$ python -m spacy init config ./config.cfg --lang en --pipeline ner
```

* init config: the command to run
* config.cfg: output path for the generated config
* --lang: language class of the pipeline, e.g. en for English
* --pipeline: comma-separated names of components to include



### Training a pipeline (1)

* all you need is the config.cfg and the training and development data
* config settings can be overwritten on the command line


```python
$ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy
```

* train: the command to run
* config.cfg: the path to the config file
* --output: the path to the output directory to save the trained pipeline
* --paths.train: override with path to the training data
* --paths.dev: override with path to the evaluation data



### Loading a trained pipeline

* output after training is a regular loadable spaCy pipeline
    * model-last: last trained pipeline
    * model-best: best trained pipeline

* load it with spacy.load


```python
import spacy

nlp = spacy.load("/path/to/output/model-best")
doc = nlp("iPhone 11 vs iPhone 8: What's the difference?")
print(doc.ents)
```


### Tip: Packaging your pipeline

* [spacy package](https://spacy.io/api/cli#package): create an installable Python package containing your pipeline
* easy to version and deploy

```python
python -m spacy package /path/to/output/model-best ./packages --name my_pipeline --version 1.0.0
```

```python
$ cd ./packages/en_my_pipeline-1.0.0
$ pip install dist/en_my_pipeline-1.0.0.tar.gz
```
Load and use the pipeline after installation:

```python
nlp = spacy.load("en_my_pipeline")
```