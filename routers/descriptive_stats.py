from fastapi import APIRouter, Query
from typing import List
from linguaf import descriptive_statistics as ds
from pydantic import BaseModel

router = APIRouter()

class DocumentRequest(BaseModel):
    documents: List[str]
    ignore_spaces: bool = True

@router.post('/charCount')
def get_CharCount(request: DocumentRequest):
    if len(request.documents) != 0:
        return {"charCount": ds.char_count(request.documents, request.ignore_spaces)}
    return {"Empty String"}


class LetterCountRequest(BaseModel):
    documents: List[str]
    ignore_spaces: bool = True
    ignore_digits: bool = True


@router.post('/letterCount')
def get_LetterCount(request: LetterCountRequest):
    return {"letterCount": ds.letter_count(request.documents, request.ignore_spaces, request.ignore_digits)}


class PunctuationCountRequest(BaseModel):
    documents: List[str]


@router.post('/punctuationCount')
def get_PunctuationCount(request: PunctuationCountRequest):
    return {"punctuationCount": ds.punctuation_count(request.documents)}


class DigitCountRequest(BaseModel):
    documents: List[str]


@router.post('/digitCount')
def get_DigitCount(request: DigitCountRequest):
    return {"digitCount": ds.digit_count(request.documents)}


class SyllableCountRequest(BaseModel):
    words: List[str]
    lang: str = 'en'


@router.post('/syllableCount')
def get_SyllableCount(request: SyllableCountRequest):
    return {"syllableCount": ds.syllable_count(request.words, request.lang)}


class NumberOfNSyllableWordsRequest(BaseModel):
    words: List[str]
    lang: str = 'en'
    n: List[int] = Query([1, 2])


@router.post('/numberOfNSyllableWords')
def get_NumberOfNSyllableWords(request: NumberOfNSyllableWordsRequest):
    return {"numberOfNSyllableWords": ds.number_of_n_syllable_words(request.words, request.lang, tuple(request.n))}


class GetWordsRequest(BaseModel):
    documents: List[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/getWords')
def get_Words(request: GetWordsRequest):
    return {"words": ds.get_words(request.documents, request.lang, request.remove_stopwords)}


class TokenizeRequest(BaseModel):
    text: str
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/tokenize')
def tokenize_Text(request: TokenizeRequest):
    return {"tokens": ds.tokenize(request.text, request.remove_stopwords, request.lang)}


class AvgSyllablePerWordRequest(BaseModel):
    documents: List[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/avgSyllablePerWord')
def get_AvgSyllablePerWord(request: AvgSyllablePerWordRequest):
    return {"avgSyllablePerWord": ds.avg_syllable_per_word(request.documents, request.lang, request.remove_stopwords)}


class SentenceCountRequest(BaseModel):
    documents: List[str]


@router.post('/sentenceCount')
def get_SentenceCount(request: SentenceCountRequest):
    return {"sentenceCount": ds.sentence_count(request.documents)}


class AvgWordLengthRequest(BaseModel):
    documents: List[str]
    lang: str = 'en'


@router.post('/avgWordLength')
def get_AvgWordLength(request: AvgWordLengthRequest):
    return {"avgWordLength": ds.avg_word_length(request.documents, request.lang)}


class AvgSentenceLengthRequest(BaseModel):
    documents: List[str]
    lang: str = 'en'


@router.post('/avgSentenceLength')
def get_AvgSentenceLength(request: AvgSentenceLengthRequest):
    return {"avgSentenceLength": ds.avg_sentence_length(request.documents, request.lang)}


class GetNGramsRequest(BaseModel):
    documents: List[str]
    n: int = 2
    lang: str = 'en'


@router.post('/getNGrams')
def get_NGrams(request: GetNGramsRequest):
    return {"ngrams": ds.get_ngrams(request.documents, request.n, request.lang)}


class GetLexicalItemsRequest(BaseModel):
    documents: List[str]
    remove_stopwords: bool = False
    lang: str = 'en'
    

@router.post('/getLexicalItems')
def get_LexicalItems(request: GetLexicalItemsRequest):
    return {"lexicalItems": ds.get_lexical_items(request.documents, request.remove_stopwords, request.lang)}


class AvgWordsPerSentenceRequest(BaseModel):
    documents: List[str]


@router.post('/avgWordsPerSentence')
def get_AvgWordsPerSentence(request: AvgWordsPerSentenceRequest):
    return {"avgWordsPerSentence": ds.avg_words_per_sentence(request.documents)}