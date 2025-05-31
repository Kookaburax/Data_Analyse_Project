# app/main.py
from fastapi import FastAPI
from app.api import upload

app = FastAPI(
    title="Data Quality SaaS",
    description="API de test automatique de la qualité des données",
    version="0.1.0"
)

# Inclure les routes
app.include_router(upload.router, prefix="/api")