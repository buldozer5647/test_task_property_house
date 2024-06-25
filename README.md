
# A test for Middle Python Developer position at Property House

Task: create a REST API using Python that will interact with the NLTK library. This API will be used by the frontend application to perform various text processing operations.

I decided to use FastAPI library.

To start a project you should:
- clone the repository
- install all python libraries from requirements.txt
```
pip install -r requirements.txt
```
- on the initialization run uncomment the necessary nltk.download() lines
```python
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
```
- then you can run a code with a command
```
fatapi dev main.py
```