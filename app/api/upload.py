from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from app.services.quality_checks import basic_quality_report

router = APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Seuls les fichiers CSV sont acceptés.")
    
    contents = await file.read()
    df = pd.read_csv(pd.io.common.BytesIO(contents))

    report = basic_quality_report(df)
    return report