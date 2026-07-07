from fastapi import FastAPI
from agent import triage
from models import TicketInput

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Potens AI Triage Agent Running"}


@app.post("/triage")
def analyze(ticket: TicketInput):
    return triage(ticket.text)