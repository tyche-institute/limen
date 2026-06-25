from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

@app.get("/aggregates.json")
async def get_aggregates():
    data_path = Path(__file__).parent / "aggregates.json"
    with data_path.open() as f:
        data = json.load(f)
    return data