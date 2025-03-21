from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
def serve_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API to send user input to backend
@app.post("/insert")
def insert_data(text: str):
    response = requests.post("http://backend:9567/insert", json={"text": text})
    return response.json()

@app.get("/get")
def get_best_match(query: str):
    response = requests.get(f"http://backend:9567/get?query={query}")
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9567)
