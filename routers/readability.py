from fastapi import APIRouter
from pydantic import BaseModel
from linguaf.descriptive_statistics import get_words, syllable_count, avg_word_length, \
    number_of_n_syllable_words, sentence_count, avg_words_per_sentence
from linguaf import __check_bool_param, __check_documents_param, __check_lang_param

router = APIRouter()


class FleschReadingEaseRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/fleschReadingEase')
def calculate_flesch_reading_ease(request: FleschReadingEaseRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    words = get_words(request.documents, request.lang, request.remove_stopwords)
    asl = avg_words_per_sentence(request.documents, request.lang, request.remove_stopwords)
    syl_total = syllable_count(words, request.lang)

    if request.lang == 'en':
        return {"fleschReadingEase": 206.835 - 1.015*asl - 84.6*(syl_total/len(words))}
    elif request.lang == 'ru':
        return {"fleschReadingEase": 206.835 - 1.3*asl - 60.1*(syl_total/len(words))}


class FleschKincaidGradeRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/fleschKincaidGrade')
def calculate_flesch_kincaid_grade(request: FleschKincaidGradeRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    words = get_words(request.documents, request.lang, request.remove_stopwords)
    asl = avg_words_per_sentence(request.documents, request.lang, request.remove_stopwords)
    syl_total = syllable_count(words, request.lang)

    if request.lang == 'en':
        return {"fleschKincaidGrade": 0.39*asl + 11.8*(syl_total/len(words)) - 15.59}
    elif request.lang == 'ru':
        return {"fleschKincaidGrade": 0.5*asl + 8.4*(syl_total/len(words)) - 15.59}


class AutomatedReadabilityIndexRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/automatedReadabilityIndex')
def calculate_automated_readability_index(request: AutomatedReadabilityIndexRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    asl = avg_words_per_sentence(request.documents, request.lang, request.remove_stopwords)
    awl = avg_word_length(request.documents, request.lang, request.remove_stopwords)

    return {"automatedReadabilityIndex": 0.5*asl + 4.71*awl - 21.43}


class AutomatedReadabilityIndexSimpleRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/automatedReadabilityIndexSimple')
def calculate_automated_readability_index_simple(request: AutomatedReadabilityIndexSimpleRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    asl = avg_words_per_sentence(request.documents, request.lang, request.remove_stopwords)
    awl = avg_word_length(request.documents, request.lang, request.remove_stopwords)

    return {"automatedReadabilityIndexSimple": asl + 9.0*awl}


class ColemanReadabilityRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/colemanReadability')
def calculate_coleman_readability(request: ColemanReadabilityRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    words = get_words(request.documents, request.lang, request.remove_stopwords)
    nws_one = number_of_n_syllable_words(words, request.lang, (1, 2))

    return {"colemanReadability": 1.29*(100*nws_one/len(words)) - 38.45}


class EasyListeningRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'
    remove_stopwords: bool = False


@router.post('/easyListening')
def calculate_easy_listening(request: EasyListeningRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)
    __check_bool_param(request.remove_stopwords)

    nst = sentence_count(request.documents)
    words = get_words(request.documents, request.lang, request.remove_stopwords)
    nws_more_two = number_of_n_syllable_words(words, request.lang, (2, 15))

    return {"easyListening": nws_more_two/nst}
