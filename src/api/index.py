from fastapi import FastAPI

app = FastAPI()

@app.post("/api")
def parse_email():
    return {"message": "Hello World"}