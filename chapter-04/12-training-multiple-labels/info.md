### Part 1

* Complete the token offsets for the "WEBSITE" entities in the data.


### Part 2

Q: A model was trained with the data you just labelled, plus a few thousand similar examples. After training, it’s doing great on "WEBSITE", but doesn’t recognize "PERSON" anymore. Why could this be happening?

A: The training data included no examples of "PERSON", so the model learned that this label is incorrect.

Response: If "PERSON" entities occur in the training data but aren’t labelled, the model will learn that they shouldn’t be predicted. Similarly, if an existing entity type isn’t present in the training data, the model may ”forget” and stop predicting it.


### Part 3

* Update the training data to include annotations for the "PERSON" entities “PewDiePie” and “Alexis Ohanian”.