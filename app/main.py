from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {
        "message": "Home Expense Manager API",
        "status": "online"
        }