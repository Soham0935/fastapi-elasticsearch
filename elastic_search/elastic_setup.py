from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Elasticsearch URL (this will be the container name in Docker)
ELASTICSEARCH_URL = "http://elasticsearch:9200/documents/_doc/"

class Document(BaseModel):
    text: str

@app.post("/insert")
def insert_document(doc: Document):
    data = {"text": doc.text}
    response = requests.post(ELASTICSEARCH_URL, json=data)
    return {"message": "Document inserted" if response.status_code == 201 else "Error inserting document"}

@app.get("/get")
def get_best_match():
    search_query = {
        "query": {"match_all": {}}
    }
    response = requests.get(f"{ELASTICSEARCH_URL}_search", json=search_query)
    if response.status_code == 200:
        hits = response.json().get("hits", {}).get("hits", [])
        if hits:
            best_match = hits[0]["_source"]["text"]
            return {"best_match": best_match}
    return {"best_match": "No documents found"}
