from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
import pandas as pd
from io import BytesIO
import json

from app.services.quality_checks import basic_quality_report, apply_rules

router = APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Seuls les fichiers CSV sont acceptés.")

    contents = await file.read()

    try:
        df = pd.read_csv(BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur de lecture du fichier : {str(e)}")

    report = basic_quality_report(df)
    return JSONResponse(content=report)

@router.post("/upload-with-rules")
async def upload_with_rules(
    file: UploadFile = File(...),
    rules: str = Form(None)  # <- ici on reçoit la chaîne JSON
):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Seuls les fichiers CSV sont acceptés.")

    contents = await file.read()

    try:
        df = pd.read_csv(BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur de lecture du fichier : {str(e)}")

    report = basic_quality_report(df)

    if rules:
        try:
            parsed_rules = json.loads(rules)
            print("✅ Règles reçues :", parsed_rules)
            custom = apply_rules(df, parsed_rules["rules"])
            report["custom_rules"] = custom
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erreur parsing JSON rules : {str(e)}")

    return JSONResponse(content=report)
