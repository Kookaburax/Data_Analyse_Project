# 🧪 Data Quality Checker API

Une API FastAPI qui permet d'évaluer automatiquement la qualité de fichiers CSV selon des règles définies par l'utilisateur.

---

## 🚀 Fonctionnalités

- ✅ Vérification de valeurs nulles
- ✅ Détection de lignes dupliquées
- ✅ Typage des colonnes
- ✅ **Règles personnalisées** :
  - Longueur minimale de chaîne (`length`)
  - Unicité d'une colonne (`unique`)
  - Format via regex (`regex`)

---

## ⚙️ Installation locale

```bash
git clone https://github.com/Kookaburax/Data_Analyse_Project.git
cd Data_Analyse_Project
pip install -r requirements.txt
uvicorn app.main:app --reload

📖 Accès Swagger UI
Une fois l'API lancée :
👉 http://localhost:8000/docs

Endpoints principaux :
Endpoint	Description
POST /api/upload	Upload d’un CSV simple, sans règle
POST /api/upload-with-rules	Upload + règles personnalisées

🧪 Exemple d'appel avec règles personnalisées
bash
Copier
Modifier
curl -X POST "http://localhost:8000/api/upload-with-rules" \
  -F "file=@data/test_data_rules.csv" \
  -F 'rules={"rules":{"name":{"type":"length","min_length":3},"email":{"type":"regex","pattern":"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$"},"id":{"type":"unique"}}}'
📄 Exemple de JSON de règles
json
Copier
Modifier
{
  "rules": {
    "name": {
      "type": "length",
      "min_length": 3
    },
    "email": {
      "type": "regex",
      "pattern": "^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$"
    },
    "id": {
      "type": "unique"
    }
  }
}
📁 Structure du projet
css
Copier
Modifier
.
├── app/
│   ├── main.py
│   ├── api/
│   │   └── upload.py
│   ├── services/
│   │   └── quality_checks.py
│   ├── models/
│   │   └── validation.py
├── data/
│   ├── test_data_rules.csv
│   └── rules.json
├── requirements.txt
├── README.md
📌 À venir
📊 Test numérique (intervalle)

📄 Rapport HTML

🖼 Interface utilisateur (Streamlit)

👨‍💻 Auteur
Axel EMERIC – 2025