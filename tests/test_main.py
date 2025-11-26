from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_quote_calculation():
    payload = {
        "client": {"name": "Test", "contact": "a@b.com", "lang": "en"},
        "currency": "SAR",
        "items": [{"sku": "X1", "qty": 2, "unit_cost": 100, "margin_pct": 10}],
        "delivery_terms": "DAP",
        "notes": "Test note"
    }
    response = client.post("/quote", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["grand_total"] == 220  # 100*1.1*2
    assert "Test" in data["email_draft"]


# # test_main.py
# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)

# sample_request_en = {
#     "client": {"name": "Gulf Eng.", "contact": "omar@client.com", "lang": "en"},
#     "currency": "SAR",
#     "items": [
#         {"sku": "ALR-SL-90W", "qty": 120, "unit_cost": 240.0, "margin_pct": 22},
#         {"sku": "ALR-OBL-12V", "qty": 40, "unit_cost": 95.5, "margin_pct": 18}
#     ],
#     "delivery_terms": "DAP Dammam, 4 weeks",
#     "notes": "Client asked for spec compliance with Tarsheed."
# }

# def test_quote_en():
#     response = client.post("/quote", json=sample_request_en)
#     assert response.status_code == 200
#     data = response.json()
#     assert "email_draft" in data
#     assert "Dear Gulf Eng." in data["email_draft"]
#     assert data["grand_total"] == 39643.6
