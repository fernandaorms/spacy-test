# Spacy - NER

## Enviroment Setup

#### 1. Create a Virtual Environment

In the terminal, navigate to the root folder of the project and run:


##### (Windows)
```
python -m venv **venv**
.\\**venv**\Scripts\activate
```

##### (Linux - Ubuntu)
```
sudo apt install python3.10-venv
python3 -m venv **venv**
source **venv**/bin/activate
```

After executing the commands, the command prompt will show the name of the virtual environment in parentheses **(venv)**



#### 2. Install Spacy Dependencies

With the **venv** activated, run the commands:

---
##### (Windows)
```
python.exe -m pip install --upgrade pip
```

##### (Linux - Ubuntu)
```
pip install --upgrade pip
```

##### (All)
```
pip install -U pip setuptools wheel
pip install -U spacy *pygls*
python -m spacy download en_core_web_sm
```

After that, spaCy should be configured correctly.

- Install the 'spaCy' extension for VS Code.
- Test if all the configurations were installed correctly:

```python
python -m spacy info 
```

#### 3. Testing

Create a file named **teste.py** to test the model loading and include the following code

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(token.text, token.pos_, token.dep_)
```


## Usefull Commands

- deactivate: stop the terminal
- .\\venv\Scripts\activate 
- source **venv**/bin/activate (run terminal - Windows)