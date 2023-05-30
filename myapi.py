from fastapi import FastAPI, Query
from linguaf import descriptive_statistics as ds
from typing import List
from pydantic import BaseModel
from routers import router as api_app

app = FastAPI()
app.include_router(api_app, prefix="/api")

# Existing APIs

@app.get('/')
def index():
    return {"name": "First Data"}

# Descriptive Stats APIs
# class DocumentRequest(BaseModel):
#     documents: List[str]
#     ignore_spaces: bool = True


# @app.post('/charCount')
# def get_CharCount(request: DocumentRequest):
#     if len(request.documents) != 0:
#         return {"charCount": ds.char_count(request.documents, request.ignore_spaces)}
#     return {"Empty String"}



