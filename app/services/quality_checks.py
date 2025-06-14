import pandas as pd
import numpy as np
from typing import Dict, Any

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

def apply_rules(df: pd.DataFrame, rules: Dict[str, Any]) -> dict:
    results = {}

    for col, rule in rules.items():
        if col not in df.columns:
            results[col] = "Colonne introuvable"
            continue

        series = df[col]

        # Règle 1 : unicité
        if rule["type"] == "unique":
            duplicated = series[series.duplicated()]
            results[col] = {
                "type": "unique",
                "duplicate_count": int(duplicated.count()),
                "duplicate_values": duplicated.dropna().tolist()
            }

        # Règle 2 : regex (ex: email)
        elif rule["type"] == "regex":
            pattern = rule.get("pattern")
            if not pattern:
                results[col] = "Regex non fournie"
                continue
            invalid = series[~series.astype(str).str.match(pattern, na=False)]
            results[col] = {
                "type": "regex",
                "invalid_count": int(invalid.count()),
                "invalid_values": invalid.dropna().tolist()
            }

        # Règle 3 : longueur minimale
        elif rule["type"] == "length":
            min_len = rule.get("min_length", 0)
            invalid = series[series.astype(str).str.len() < min_len]
            results[col] = {
                "type": "length",
                "min_length": min_len,
                "invalid_count": int(invalid.count()),
                "invalid_values": invalid.dropna().tolist()
            }

        else:
            results[col] = f"Type de règle non reconnu : {rule['type']}"

    return results