from fastapi import APIRouter
from pydantic import BaseModel
from linguaf.descriptive_statistics import get_sentences, get_words
from linguaf import __check_documents_param, __check_lang_param
from natasha import Segmenter, NewsSyntaxParser, Doc, NewsEmbedding
import spacy

router = APIRouter()


class MeanDependencyDistanceRequest(BaseModel):
    documents: list[str]
    lang: str = 'en'


@router.post('/meanDependencyDistance')
def calculate_mean_dependency_distance(request: MeanDependencyDistanceRequest):
    __check_documents_param(request.documents)
    __check_lang_param(request.lang)

    dd = 0
    sentences = get_sentences(request.documents)
    words = get_words(request.documents, request.lang)

    for text in sentences:
        if request.lang == 'ru':
            segmenter = Segmenter()
            emb = NewsEmbedding()
            syntax_parser = NewsSyntaxParser(emb)
            doc = Doc(text)
            doc.segment(segmenter)
            doc.parse_syntax(syntax_parser)
            for t in doc.tokens:
                dd += abs(int(t.head_id.split('_')[1]) - int(t.id.split('_')[1]))
        elif request.lang == 'en':
            try:
                nlp = spacy.load("en_core_web_sm")
            except:
                spacy.cli.download('en_core_web_sm')  # required for english language
                nlp = spacy.load("en_core_web_sm")

            doc = nlp(text)
            for token in doc:
                dd += abs(token.head.i - token.i)

    return {"meanDependencyDistance": dd / (len(words) - len(sentences))}
