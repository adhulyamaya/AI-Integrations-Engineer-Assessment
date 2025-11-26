# # main.py
# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# from typing import List

# app = FastAPI(
#     title="Quotation Microservice",
#     description="Generates quotation totals and email drafts (AR/EN). Supports mock LLM for local use.",
#     version="1.0"
# )

# # -------------------
# # Pydantic Models
# # -------------------

# class Item(BaseModel):
#     sku: str = Field(..., description="Product SKU or model number")
#     qty: int = Field(..., gt=0, description="Quantity")
#     unit_cost: float = Field(..., gt=0, description="Unit cost of the item")
#     margin_pct: float = Field(..., ge=0, description="Margin percentage")

# class Client(BaseModel):
#     name: str
#     contact: str
#     lang: str = Field("en", description="Preferred language: 'en' or 'ar'")

# class QuoteRequest(BaseModel):
#     client: Client
#     currency: str
#     items: List[Item]
#     delivery_terms: str
#     notes: str

# class QuoteItemResponse(BaseModel):
#     sku: str
#     qty: int
#     unit_price: float
#     line_total: float

# class QuoteResponse(BaseModel):
#     items: List[QuoteItemResponse]
#     grand_total: float
#     email_draft: str

# # -------------------
# # Mock LLM Function
# # -------------------

# def mock_llm(client_name, grand_total, currency, delivery_terms, notes, lang="en") -> str:
#     """Generate email draft (mock LLM)"""
#     if lang.lower() == "ar":
#         return f"""
# عميلنا العزيز {client_name}،

# نرفق لكم عرض السعر. المجموع النهائي: {grand_total:,.2f} {currency}
# التسليم: {delivery_terms}
# ملاحظات: {notes}

# مع التحية،
# فريق المبيعات
# """
#     else:
#         return f"""
# Dear {client_name},

# Please find your quotation. Total amount: {grand_total:,.2f} {currency}
# Delivery: {delivery_terms}
# Notes: {notes}

# Regards,
# Sales Team
# """

# # -------------------
# # Utility function
# # -------------------

# def calculate_line_total(unit_cost: float, margin_pct: float, qty: int) -> float:
#     """Calculate unit price including margin and line total"""
#     unit_price = unit_cost * (1 + margin_pct / 100)
#     line_total = unit_price * qty
#     return round(unit_price, 2), round(line_total, 2)

# # -------------------
# # API Endpoint
# # -------------------

# @app.post("/quote", response_model=QuoteResponse, summary="Create Quote", description="Calculates line totals, grand total, and generates an email draft (AR/EN).")
# def create_quote(request: QuoteRequest):
#     items_response = []
#     grand_total = 0.0

#     for item in request.items:
#         unit_price, line_total = calculate_line_total(item.unit_cost, item.margin_pct, item.qty)
#         items_response.append(QuoteItemResponse(
#             sku=item.sku,
#             qty=item.qty,
#             unit_price=unit_price,
#             line_total=line_total
#         ))
#         grand_total += line_total

#     # Use mock LLM to generate email draft
#     email_draft = mock_llm(
#         client_name=request.client.name,
#         grand_total=grand_total,
#         currency=request.currency,
#         delivery_terms=request.delivery_terms,
#         notes=request.notes,
#         lang=request.client.lang
#     )

#     return QuoteResponse(
#         items=items_response,
#         grand_total=round(grand_total, 2),
#         email_draft=email_draft
#     )

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
