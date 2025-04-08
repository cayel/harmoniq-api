# Harmoniq API

API FastAPI pour la gestion des classements musicaux.

## 🚀 Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
```

2. Activer l'environnement virtuel :
```bash
source venv/bin/activate  # Sur Linux/Mac
venv\Scripts\activate  # Sur Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Lancer l'API :
```bash
uvicorn main:app --reload
```

API sera accessible à :

- [http://127.0.0.1](http://127.0.0.1):8000 (interface utilisateur)

- [http://127.0.0.1](http://127.0.0.1):8000/docs (interface Swagger)


## 🛠️ Développement
    
### Tests

Pour exécuter les tests unitaires :

```bash
pytest
```

Pour exécuter les tests avec la couverture de code :

```bash
pytest --cov=main --cov-report=term-missing
```

## 🚀 Déploiement

Le projet est configuré pour le déploiement sur Vercel via vercel.json.


