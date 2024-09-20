### 1. nlp.pipe()
O nlp.pipe() processa múltiplos textos em lote de forma eficiente, utilizando o pipeline completo do modelo (tokenização, lematização, POS tagging, reconhecimento de entidades, etc.).

* Uso principal: Processar várias sentenças ou textos grandes de forma mais rápida.
* Retorno: Um iterador de objetos Doc, que você pode transformar em uma lista, se necessário.

Exemplo:
```python
texts = ["I like apples.", "She loves oranges.", "We enjoy bananas."]
docs = nlp.pipe(texts)  # Iterador de objetos Doc

for doc in docs:
    print([token.text for token in doc])
```

* Vantagem: nlp.pipe() é otimizado para processamento em lote, tornando-o mais rápido e eficiente em comparação com o uso de nlp() repetidamente em cada texto.

### 2. nlp.make_doc()

O nlp.make_doc() apenas realiza a tokenização de um texto, criando um objeto Doc sem passar pelo pipeline completo de processamento.

* Uso principal: Quando você só quer transformar um texto em tokens, sem aplicar as outras etapas do pipeline (como análise gramatical ou entidades nomeadas).
* Retorno: Um objeto Doc com tokens, mas sem outras anotações (como POS tagging, dependências, etc.).

Exemplo:
```python
doc = nlp.make_doc("I like apples.")
print([token.text for token in doc])  # Apenas tokeniza o texto
```

* Vantagem: É útil quando você precisa apenas da tokenização, sem o custo adicional de passar por todo o pipeline NLP.