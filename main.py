import nltk
from fastapi import FastAPI
from pydantic import BaseModel

# uncomment on initial setup
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

class Item(BaseModel):
    text: str

app = FastAPI()

@app.post("/tokenize")
async def tokenize_text(item: Item):
    text = item.text

    tokens = nltk.word_tokenize(text)
    
    return {"tokens": tokens}

@app.post("/pos_tag")
async def pos_tag_text(item: Item):
    text = item.text

    tokens = nltk.word_tokenize(text)

    tagged = nltk.pos_tag(tokens)

    res = dict()

    for k, v in tagged:
        res[k] = v

    return tagged

@app.post("/ner")
async def ner_text(item: Item):
    text = item.text

    tokens = nltk.word_tokenize(text)

    tagged = nltk.pos_tag(tokens)

    entities = nltk.chunk.ne_chunk(tagged)

    res = []

    # initialization of array of named entities
    for subtree in entities.subtrees():
        if subtree.label() and subtree.label() != "S":
            entity_label = subtree.label()
            tokens_in_entity = [token for token, pos in subtree.leaves()]
            res.extend([(token, entity_label) for token in tokens_in_entity])

    return res
