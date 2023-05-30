# LinguaF EngTutor

**LinguaF provides an easy access for researchers and developers to methods of quantitative language analysis, such as: readability, complexity, diversity, and other descriptive statistics.**

## Usage

For e.g.POST `/api/ds/charCount` where the body request is
```json
{
  "documents": [
    "string"
  ],
  "ignore_spaces": true
}
``` 

will return you a JSON response of
```json
{
  "charCount": 6
}
```

## API Endpoints

Note: Different endpoints have different schema and request bodies, for other endpoints such as lexical_div/readability/synthetical_complexity please refer to http://3.1.194.140/docs for more information

The following descriptive statistics are supported (`descriptive_stats.py` module):

* Number of characters `/api/ds/charCount`
* Number of letters `/api/ds/letterCount`
* Number of punctuation characters `/api/ds/punctuationCount`
* Number of digits `/api/ds/digitCount`
* Number of syllables `/api/ds/syllableCount`
* Number of sentences `/api/ds/sentenceCount`
* Number of n-syllable words `/api/ds/numberOfNSyllableWords`
* Average syllables per word `/api/ds/avgSyllablePerWord`
* Average word length `/api/ds/avgWordLength`
* Average sentence length `/api/ds/avgSentenceLength`
* Get n-grams `/api/ds/getNGrams`
* Average words per sentence `/api/ds/avgWordsPerSentence`
* Get Lexical Items `/api/ds/getLexicalItems`
* Tokenize text `/api/ds/tokenize`
* Get words `/api/ds/getWords`
  

### Deployment
1. Spin up ec2 server on AWS account
2. SSH into your instance andd git clone https://github.com/me-tech-dev/FastAPIEngTut.git into your server
3. cd to FastAPIEngTut
4. pip install linguaf
5. pip install uvicorn
6. pip install fastapi
7. type screen which will redirect you to a screen
8. run python3 -m uvicorn myapi:app in the screen where myapi.py as entry pt
9. In the event you get a 502 error, it's because the server has crashed but creating a screen will ensure the api is up
10. Typing screen -ls allows u to see all screens and screen -r 11011 goes back into the screen where 11011 is the id you get from running screen -ls

## Language Support

At the moment, library supports English and Russian languages for all the methods.

