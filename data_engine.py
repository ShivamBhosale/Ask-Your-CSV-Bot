import pandas as pd

def analyze_data(df: pd.DataFrame, question: str) -> dict:
    question = question.lower()

    if "average" in question:
        col = extract_column(df, question)
        value = df[col].mean()
        return {"operation": "average", "column": col, "value": value}

    if "maximum" in question or "max" in question:
        col = extract_column(df, question)
        value = df[col].max()
        return {"operation": "max", "column": col, "value": value}

    if "minimum" in question or "min" in question:
        col = extract_column(df, question)
        value = df[col].min()
        return {"operation": "min", "column": col, "value": value}

    raise ValueError("Unsupported question")


def extract_column(df: pd.DataFrame, question: str) -> str:
    for col in df.columns:
        if col.lower() in question:
            return col
    raise ValueError("Column not found in question")
