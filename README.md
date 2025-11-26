# Quotation Microservice

A **FastAPI** microservice to generate quotations with **line totals, grand total**, and **email drafts** in **Arabic and English** using a **mock LLM** for local testing.

---

## Features

- Calculate **unit price including margin** and **line totals** per item  
- Compute **grand total** of all items  
- Generate **email drafts in English or Arabic** based on client preference  
- **Mock LLM** allows local testing without AI API keys  
- Fully tested with **pytest**  
- Ready for **Docker containerization**  

---

## Folder Structure

Quotation-Microservice/
│
├─ main.py # FastAPI application
├─ services.py # Business logic (calculations, email draft)
├─ tests/
│ ├─ test_main.py # pytest tests
├─ requirements.txt # Python dependencies
├─ Dockerfile # Docker containerization
└─ README.md # Project explanation


---

## API Endpoint

### POST `/quote`

**Description:** Calculate line totals, grand total, and generate email draft (AR/EN) based on client language.

**Request Body (JSON):**

```json Request body
{
  "client": {
    "name": "Gulf Eng.",
    "contact": "omar@client.com",
    "lang": "en"
  },
  "currency": "SAR",
  "items": [
    {
      "sku": "ALR-SL-90W",
      "qty": 120,
      "unit_cost": 240.0,
      "margin_pct": 22
    },
    {
      "sku": "ALR-OBL-12V",
      "qty": 40,
      "unit_cost": 95.5,
      "margin_pct": 18
    }
  ],
  "delivery_terms": "DAP Dammam, 4 weeks",
  "notes": "Client asked for spec compliance with Tarsheed."
}
``` 
```json Response body
{
  "items": [
    {
      "sku": "ALR-SL-90W",
      "qty": 120,
      "unit_price": 292.8,
      "line_total": 35136
    },
    {
      "sku": "ALR-OBL-12V",
      "qty": 40,
      "unit_price": 112.69,
      "line_total": 4507.6
    }
  ],
  "grand_total": 39643.6,
  "email_draft": "Dear Gulf Eng.,\n\nPlease find your quotation. Total amount: 39,643.60 SAR\nDelivery: DAP Dammam, 4 weeks\nNotes: Client asked for spec compliance with Tarsheed.\n\nRegards,\nSales Team"
}
``` 
## Installation & Running Locally

# Clone repository
git clone <repo_url>
cd Quotation-Microservice

# Create virtual environment
python -m venv venv

# Activate venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app
uvicorn main:app --reload

## Run tests
python -m pytest

## Swagger UI: http://127.0.0.1:8000/docs

## Docker

# Build Docker image
docker build -t quotation-service .

# Run container
docker run -p 8000:8000 quotation-service


