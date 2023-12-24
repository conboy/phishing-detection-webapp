from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import model.predict_phishing as model

class Email(BaseModel):
    email_text: str

app = FastAPI()

@app.post("/api/process_email")
def process_email(email: Email):
    email_text = email.email_text
    phishing_probability = model.predict_phishing(email_text)
    if phishing_probability < 0.5:
        return "Not a phishing email"
    model.analyze_email(email_text)
    return {"message": phishing_probability}