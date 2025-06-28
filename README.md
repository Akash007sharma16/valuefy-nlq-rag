# Natural Language Query RAG Agent

#Submitted for: Valuefy Technical Assignment  
# Developed by: Akashdeep Sharma

---

# Overview

This is a full-stack Natural Language Query (NLQ) system built to help wealth management professionals query client and investment data using **plain English** — no SQL, no filters, just simple questions.

The project mimics how a **relationship manager** might ask:

> “Who are the top 5 clients by portfolio size?”  
> “Which relationship manager is performing best?”

And instantly receive a response — rendered as a table, chart, or text.

---

# Tech Stack

| Layer      | Tech Used             |
|------------|------------------------|
| Frontend   | React.js               |
| Backend    | FastAPI (Python)       |
| HTTP Comm. | Axios                  |
| Charts     | Chart.js               |
| Styling    | Plain CSS              |

---

# Features

- 🔍 Accepts natural language queries + remarks
- 🔁 API communication between frontend and backend
- 📊 Dynamic response types:
  - Table (e.g., portfolio summaries)
  - Bar Chart (e.g., RM performance)
  - Text (fallback or unsupported)
- 🧪 Mock logic simulating real-world AI/LLM behavior
- 🧹 Clean folder structure, cloud-deployable

---

# Project Structure
valuefy-nlq-raq/
├── backend/ → FastAPI backend (main.py, mock logic)
├── frontend/ → React.js frontend (App.js, components)
├── README.md


##Running the Project Locally

#1. Clone the Repository

```bash
git clone https://github.com/your-username/valuefy-nlq-raq.git
cd valuefy-nlq-raq

cd backend
python -m venv env
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload


Start the Frontend
cd frontend
npm install
npm start
