from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Unified and updated model
class QueryRequest(BaseModel):
    query: str
    remarks: str = "" 

# Mock MongoDB: Client profiles
client_profiles = [
    {"name": "Virat Kohli", "risk": "High", "investment": "Stocks"},
    {"name": "Alia Bhatt", "risk": "Medium", "investment": "Mutual Funds"},
    {"name": "MS Dhoni", "risk": "Low", "investment": "Bonds"},
]

# Mock MySQL: Portfolio + Relationship manager data
portfolio_data = [
    {"client": "Virat Kohli", "value": 20, "manager": "Raj"},
    {"client": "MS Dhoni", "value": 18, "manager": "Simran"},
    {"client": "Alia Bhatt", "value": 15, "manager": "Kabir"},
    {"client": "Hardik Pandya", "value": 10, "manager": "Raj"},
    {"client": "Rohit Sharma", "value": 25, "manager": "Raj"},
]

@app.post("/query")
async def handle_query(req: QueryRequest):
    q = req.query.lower()

    # Optional: log remarks 
    if req.remarks:
        print(f"User remarks: {req.remarks}")

    #  Top portfolios
    if "top portfolios" in q:
        top = sorted(portfolio_data, key=lambda x: x["value"], reverse=True)[:5]
        return {
            "type": "table",
            "data": [{"Client": p["client"], "Value (Cr)": f"₹{p['value']} Cr"} for p in top]
        }

    #  Top relationship managers
    elif "relationship manager" in q or "managers" in q:
        count = {}
        for p in portfolio_data:
            manager = p["manager"]
            count[manager] = count.get(manager, 0) + 1
        return {
            "type": "chart",
            "labels": list(count.keys()),
            "values": list(count.values())
        }

    #  Client risk profiles
    elif "risk" in q or "risk appetite" in q:
        text = "\n".join([f"{c['name']} - {c['risk']} Risk" for c in client_profiles])
        return {"type": "text", "data": text}

    # Highest holders of specific stock (mocked logic)
    elif "highest holders" in q:
        stock = q.split("of")[-1].strip().capitalize()
        return {
            "type": "table",
            "data": [
                {"Client": "Virat Kohli", "Stock": stock, "Holding": "₹10 Cr"},
                {"Client": "MS Dhoni", "Stock": stock, "Holding": "₹8 Cr"},
            ]
        }

    # Default fallback
    else:
        return {"type": "text", "data": "Sorry, I couldn’t understand the query."}
