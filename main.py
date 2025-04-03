from fastapi import FastAPI, HTTPException, Path
from pathlib import Path as FilePath  # Renommé pour éviter les conflits
from typing import List, Dict, Any
import json
import uvicorn  # Ajout de l'importation de uvicorn

app = FastAPI()

# Précharger les données du fichier rankings.json
RANKINGS_FILE = FilePath("data/rankings.json")
rankings_data: List[Dict[str, Any]] = []
if RANKINGS_FILE.exists():
    with RANKINGS_FILE.open("r", encoding="utf-8") as file:
        rankings_data = json.load(file)
else:
    print(f"Warning: {RANKINGS_FILE} not found. Rankings endpoint will return an error.")

@app.get("/")
async def root() -> Dict[str, str]:
    """Endpoint racine pour vérifier que l'API fonctionne."""
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
async def healthcheck() -> Dict[str, str]:
    """Endpoint pour vérifier la santé de l'application."""
    return {"status": "ok"}

@app.get("/rankings")
async def get_rankings() -> List[Dict[str, Any]]:
    """Endpoint pour récupérer les données des rankings."""
    if not rankings_data:
        raise HTTPException(status_code=404, detail="Rankings file not found")
    return rankings_data

@app.get("/albums/ranking/{guid}")
async def get_album_ranking(
    guid: str = Path(..., description="GUID du fichier JSON à récupérer")
) -> List[Dict[str, Any]]:
    """Endpoint pour récupérer le contenu d'un fichier JSON correspondant à un GUID."""
    file_path = FilePath(f"data/{guid}.json")
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"File with GUID '{guid}' not found")
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)  # Renvoie une liste si le fichier JSON contient une liste
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail=f"Error decoding JSON file '{guid}.json'")
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
