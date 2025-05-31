import pandas as pd
import numpy as np

def basic_quality_report(df: pd.DataFrame) -> dict:
    report = {}

    report["shape"] = df.shape
    report["missing_values"] = df.isnull().sum().to_dict()

    # Détection des doublons (en excluant 'id' si présent)
    cols_for_dupes = df.columns.drop("id") if "id" in df.columns else df.columns
    duplicated_rows_df = df[df.duplicated(subset=cols_for_dupes, keep=False)]

    # Remplacement des valeurs non JSON-compatibles dans les doublons
    duplicates_cleaned = duplicated_rows_df.replace({np.nan: None, np.inf: None, -np.inf: None})
    report["duplicate_rows"] = len(duplicates_cleaned)
    report["duplicates_detail"] = duplicates_cleaned.to_dict(orient="records")

    # Types de données
    report["dtypes"] = df.dtypes.astype(str).to_dict()

    return report