from collections import Counter
import math
from fastapi import APIRouter
from pydantic import BaseModel
from linguaf.descriptive_statistics import get_words, get_lexical_items
from linguaf import __check_bool_param, __check_documents_param, __check_lang_param

router = APIRouter()


class LexicalDensityRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/lexicalDensity')
def calculate_lexical_density(request: LexicalDensityRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    words = get_words(documents=request.documents, lang=request.lang, remove_stopwords=request.remove_stopwords)
    lex_items = get_lexical_items(documents=request.documents, remove_stopwords=request.remove_stopwords, lang=request.lang)
    return {"lexicalDensity": len(lex_items) / len(words) * 100}


class TypeTokenRatioRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/typeTokenRatio')
def calculate_type_token_ratio(request: TypeTokenRatioRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    words = get_words(documents=request.documents, lang=request.lang, remove_stopwords=request.remove_stopwords)
    num_unq = len(Counter(words).keys())
    return {"typeTokenRatio": num_unq / len(words)}


class LogTypeTokenRatioRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/logTypeTokenRatio')
def calculate_log_type_token_ratio(request: LogTypeTokenRatioRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    words = get_words(documents=request.documents, lang=request.lang, remove_stopwords=request.remove_stopwords)
    num_unq = len(Counter(words).keys())
    return {"logTypeTokenRatio": math.log(num_unq) / math.log(len(words)) if len(words) != 1 else 0}


class SummerIndexRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/summerIndex')
def calculate_summer_index(request: SummerIndexRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    words = get_words(documents=request.documents, lang=request.lang, remove_stopwords=request.remove_stopwords)
    num_unq = len(Counter(words).keys())
    if num_unq == 0:
        num_unq = 10 ** -10
    return {"summerIndex": math.log(math.log(num_unq)) / math.log(math.log(len(words))) if len(words) != 1 else 0}


class RootTypeTokenRatioRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/rootTypeTokenRatio')
def calculate_root_type_token_ratio(request: RootTypeTokenRatioRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    words = get_words(documents=request.documents, lang=request.lang, remove_stopwords=request.remove_stopwords)
    num_unq = len(Counter(words).keys())
    return {"rootTypeTokenRatio": num_unq / (len(words) ** 0.5)}
