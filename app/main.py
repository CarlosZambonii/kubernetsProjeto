from fastapi import FastAPI

app = FastAPI(
    title="Cloud Ready DevOps Lab",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "cloud-ready-devops-lab",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
