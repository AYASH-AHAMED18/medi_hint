# Symptom Guide — Python Backend (Educational Demo)

> ⚠️ **Not a medical device.** This is a learning/demo project. The
> symptom → condition mappings are small, hand-written sample data — not
> a validated clinical dataset. Never use this for real medical decisions.
> Any real deployment would require licensed medical professionals to
> build and review the dataset and model, plus regulatory review
> depending on your region.

## What it does

- You send a list of symptoms to the API.
- A small ML model (Naive Bayes, trained on synthetic data generated from
  a hand-written symptom map) returns up to 5 **possible** conditions
  with a confidence score.
- Each result includes general home-care suggestions and a clear
  "see a doctor if…" section.
- Any condition flagged `urgent: true` (e.g. possible cardiac or
  respiratory issues) is highlighted so the user is pushed toward
  professional care instead of home remedies.

## Folder structure

```
symptom-guide-backend/
├── app/
│   ├── main.py                 # FastAPI app entrypoint, CORS setup
│   ├── data/
│   │   └── conditions.py       # Symptom vocab + condition knowledge base
│   ├── models/
│   │   └── schemas.py          # Pydantic request/response models
│   ├── services/
│   │   └── predictor.py        # ML model: trains + predicts
│   └── routers/
│       └── symptoms.py         # /api/symptoms and /api/predict routes
├── frontend/
│   └── index.html              # Simple chat-style UI that calls the API
├── requirements.txt
├── run.py                      # Convenience script: python run.py
└── README.md
```

## Setup

```bash
cd symptom-guide-backend
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run the API

```bash
python run.py
```

The API will be live at `http://localhost:8000`.
Interactive API docs (Swagger UI): `http://localhost:8000/docs`

## Run the frontend

Just open `frontend/index.html` directly in your browser
(or serve it with any static file server). It calls the API at
`http://localhost:8000` by default — change `API_BASE` at the top of the
`<script>` in `index.html` if your backend runs elsewhere.

## API Reference

### `GET /api/symptoms`
Returns the list of symptom keys the model understands.

```json
{ "symptoms": ["fever", "cough", "sore_throat", ...] }
```

### `POST /api/predict`
Request:
```json
{ "symptoms": ["fever", "cough", "shortness_of_breath"] }
```

Response:
```json
{
  "input_symptoms": ["fever", "cough", "shortness_of_breath"],
  "unknown_symptoms": [],
  "any_urgent": true,
  "results": [
    {
      "name": "Possible Respiratory Infection",
      "confidence": 0.91,
      "urgent": true,
      "home_care": "...",
      "see_doctor_if": "..."
    }
  ],
  "disclaimer": "..."
}
```

## Extending it

- **Add symptoms/conditions:** edit `app/data/conditions.py`. Add the
  symptom to `SYMPTOM_VOCAB` and add/update entries in `CONDITIONS`
  with `typical_symptoms`, `urgent`, `home_care`, and `see_doctor_if`.
  The model retrains automatically at startup from this data.
- **Swap in a real dataset:** replace the synthetic data generation in
  `predictor.py` with a real (licensed, clinically-reviewed) dataset,
  and consider a more expressive model if needed.
- **Persist the model:** currently it retrains in-memory on every
  startup (fast, since the dataset is tiny). For a larger dataset,
  train offline and load a saved model file instead (e.g. with `joblib`).

## Responsible use notes

- Keep advice general (no drug names/dosages) unless a licensed medical
  professional has reviewed and approved specific guidance.
- Always keep an urgent/doctor-referral path for red-flag symptom
  combinations — never let the system's most confident answer imply
  "problem solved" for anything serious.
- If you present this as a class/research project, be explicit that it's
  a demo of an ML pipeline architecture, not a validated medical tool.
