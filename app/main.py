from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Glynac Canary Deployment Demo"}


@app.get("/health")
def health():
    return {"status": "healthy"}
