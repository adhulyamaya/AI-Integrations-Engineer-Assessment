# ---------- QUOTE CALCULATION ----------
def calculate_quote(req):
    items_response = []
    grand_total = 0.0

    for item in req.items:
        unit_price = item.unit_cost * (1 + item.margin_pct / 100)
        line_total = unit_price * item.qty
        grand_total += line_total

        items_response.append({
            "sku": item.sku,
            "qty": item.qty,
            "unit_price": round(unit_price, 2),
            "line_total": round(line_total, 2)
        })

    email_draft = generate_email(
        client_name=req.client.name,
        grand_total=round(grand_total, 2),
        currency=req.currency,
        delivery_terms=req.delivery_terms,
        notes=req.notes,
        lang=req.client.lang
    )

    return {
        "items": items_response,
        "grand_total": round(grand_total, 2),
        "email_draft": email_draft
    }

# ---------- MOCK LLM Email Generator ----------
def generate_email(client_name, grand_total, currency, delivery_terms, notes, lang):
    if lang.lower() == "ar":
        return (
            f"عميلنا العزيز {client_name}،\n\n"
            f"نرفق لكم عرض السعر. المجموع النهائي: {grand_total:,.2f} {currency}\n"
            f"التسليم: {delivery_terms}\n"
            f"ملاحظات: {notes}\n\n"
            f"مع التحية،\nفريق المبيعات"
        )
    else:
        return (
            f"Dear {client_name},\n\n"
            f"Please find your quotation. Total amount: {grand_total:,.2f} {currency}\n"
            f"Delivery: {delivery_terms}\n"
            f"Notes: {notes}\n\n"
            f"Regards,\nSales Team"
        )

