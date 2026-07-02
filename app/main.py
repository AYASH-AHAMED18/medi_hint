from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import symptoms

app = FastAPI(
    title="Symptom Guide API",
    description=(
        "Educational demo API that suggests possible conditions from a list "
        "of symptoms. NOT a medical diagnosis tool."
    ),
    version="1.0.0",
)

# Allow the frontend (served from any origin during development) to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(symptoms.router)


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Symptom Guide API is running. See /docs for API docs.",
    }
