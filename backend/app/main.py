from fastapi import FastAPI
from app.api.routes import concierge

app = FastAPI()

app.include_router(concierge.router, prefix="/concierge")

@app.get("/")
def root():
    return {"status": "Concierge backend running"}
