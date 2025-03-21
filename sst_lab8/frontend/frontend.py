from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BACKEND_URL = "http://YOUR_BACKEND_VM_IP:9657"  # Change this to your backend VM’s internal IP

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})

@app.post("/insert")
def insert_text(request: Request, text: str = Form(...)):
    response = requests.post(f"{BACKEND_URL}/insert", json={"text": text})
    return templates.TemplateResponse("index.html", {"request": request, "result": response.json().get("message", "Error")})

@app.get("/get")
def get_text(request: Request):
    response = requests.get(f"{BACKEND_URL}/get")
    best_match = response.json().get("best_match", "No data found")
    return templates.TemplateResponse("index.html", {"request": request, "result": best_match})
