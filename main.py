from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from services import calculate_quote

app = FastAPI(title="Quotation Microservice")

class Client(BaseModel):
    name: str
    contact: str
    lang: str  # 'en' or 'ar'

class Item(BaseModel):
    sku: str
    qty: int
    unit_cost: float
    margin_pct: float

class QuoteRequest(BaseModel):
    client: Client
    currency: str
    items: List[Item]
    delivery_terms: str
    notes: str

@app.post("/quote")
def create_quote(req: QuoteRequest):
    return calculate_quote(req)
