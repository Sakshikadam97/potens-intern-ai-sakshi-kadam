import json


# Tool 1: FAQ Lookup
def lookup_tool(query):

    faq = {
        "password": "Reset Password Guide",
        "payment": "Billing Support",
        "invoice": "Invoice Download"
    }

    query = query.lower()

    for key, value in faq.items():
        if key in query:
            return value

    return "No FAQ found"


# Tool 2: Similar Ticket Search
def search_tool():

    with open("data/tickets.json", "r") as f:
        tickets = json.load(f)

    return tickets[:3]


# Tool 3: Draft Response
def draft_tool(text):

    return f"""
Dear Customer,

We have received your request.

{text}

Our support team is investigating.

Regards,
Support Team
"""