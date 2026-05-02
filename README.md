# Accidental Fall Prediction and Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.2.5-lightgrey?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.2-orange?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

> A peer-reviewed, machine learning–powered web application for predicting and detecting accidental falls in elderly persons using ensemble techniques — with real-time SMS alerting for caretakers.

**Live Demo:** [https://accidental-fall.onrender.com](https://accidental-fall.onrender.com)
**Research Paper:** [IJCA Vol. 186, No. 78 — DOI: 10.5120/ijca2025924684](https://www.ijcaonline.org/archives/volume186/number78/accidental-fall-prediction-and-detection-in-elderly-persons-using-ensemble-techniques/)

---

## Table of Contents

- [Background](#background)
- [Research Publication](#research-publication)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Model Details](#model-details)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Authors](#authors)
- [Citation](#citation)
- [License](#license)

---

## Background

Accidental falls among elderly persons represent a significant and growing public health challenge. This project applies artificial intelligence and ensemble learning techniques to predict and detect fall events in real time, using a combination of physiological and environmental sensor data. Upon detecting a fall risk or confirmed fall, the system dispatches an immediate SMS alert to the patient's registered caretaker.

This work was developed as part of a published research study and is intended for use in rapid prototyping of fall detection systems, remote patient monitoring, and eldercare notification pipelines.

---

## Research Publication

This application is the implementation artefact of a peer-reviewed research paper published in the **International Journal of Computer Applications (IJCA)**:

| Field | Detail |
|---|---|
| **Title** | Accidental Fall Prediction and Detection in Elderly Persons using Ensemble Techniques |
| **Authors** | Michael Osiako Afote, Fati Oiza Ochepa |
| **Journal** | International Journal of Computer Applications (IJCA) |
| **Publisher** | Foundation of Computer Science (FCS), NY, USA |
| **Volume / Issue** | Volume 186, Number 78 |
| **Pages** | 32–36 |
| **Year** | 2025 |
| **DOI** | [10.5120/ijca2025924684](https://doi.org/10.5120/ijca2025924684) |
| **ISSN** | 0975-8887 |

---

## Features

- **Browser-based prediction form** — submit physiological and environmental readings directly from any device.
- **Ensemble ML prediction** — uses a Bagged SVC model trained on real-world fall indicator data.
- **Real-time SMS alerts** — notifies a registered caretaker when a fall risk or fall event is detected.
- **Asynchronous submission** — form data is submitted via JavaScript without a full page reload.
- **REST API endpoint** — `/predict` accepts JSON payloads, enabling integration with IoT devices or mobile apps.
- **Clean health-tech UI** — material-inspired dashboard styled with custom CSS.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.10+, Flask 2.2.5 |
| ML / Data | scikit-learn 1.5.2, pandas 2.1.4, numpy 1.26.4 |
| Notifications | requests 2.31.0 (SMS gateway) |
| Production server | Gunicorn |
| Frontend | HTML5, CSS3, Vanilla JavaScript |

---

## Project Structure

```
accidental-fall-prediction/
├── app.py                  # Flask application and prediction logic
├── requirements.txt        # Python package dependencies
├── models/
│   └── baggedsvc.pkl       # Serialized Bagged SVC ensemble model
├── templates/
│   └── index.html          # Web interface
├── static/
│   └── style.css           # Dashboard styling
├── fall.ipynb              # Exploratory analysis and model development notebook
├── LICENSE
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` package manager
- The serialized model file `models/baggedsvc.pkl` (included in the repository)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/accidental-fall-prediction.git
cd accidental-fall-prediction
```

2. **Create and activate a virtual environment:**

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Confirm the model file is in place:**

```bash
ls models/baggedsvc.pkl
```

---

## Usage

### Start the development server

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

### Submit a prediction

1. Fill in the form fields with the patient's current readings:
   - **Name** — patient identifier
   - **Caretaker Phone Number** — receives SMS alerts
   - **Distance** — proximity sensor reading
   - **Pressure** — environmental or wearable pressure value
   - **Heart Rate Variability (HRV)** — milliseconds
   - **Sugar Level** — blood glucose reading
   - **SpO2 Level** — blood oxygen saturation (%)
   - **Accelerometer Value** — motion/impact reading

2. Click **Predict**.
3. The result is displayed inline on the page.
4. If a **fall risk** or **fall event** is detected, an SMS alert is automatically sent to the caretaker's phone number.

### API endpoint

The `/predict` route accepts a `POST` request with a JSON body:

```json
{
  "name": "John Doe",
  "phone": "+2348012345678",
  "distance": 1.2,
  "pressure": 101.3,
  "hrv": 45,
  "sugar": 110,
  "spo2": 97,
  "accelerometer": 0.85
}
```

**Response:**

```json
{
  "message": "Fall risk detected. Alert sent to caretaker."
}
```

---

## Model Details

The predictive model uses a **Bagging ensemble** approach combining:

- Random Forest (RF)
- Logistic Regression (LR)
- Support Vector Classifier (SVC)
- Decision Tree (DT)

Training data comprised both **physiological indicators** (HRV, SpO2, blood sugar) and **environmental/motion indicators** (distance, pressure, accelerometer). The serialized model is stored as `models/baggedsvc.pkl` and loaded at application startup.

For full methodology, feature engineering details, and evaluation results, refer to the [published paper](https://www.ijcaonline.org/archives/volume186/number78/accidental-fall-prediction-and-detection-in-elderly-persons-using-ensemble-techniques/).

---

## Configuration

Before deploying to production, update the following in `app.py`:

| Setting | Description |
|---|---|
| SMS credentials | Replace hardcoded API key and sender ID with environment variables |
| SMS provider URL | Update `send_sms()` with your gateway's endpoint |
| Secret key | Set `app.secret_key` via an environment variable |

**Recommended approach using environment variables:**

```python
import os

SMS_API_KEY = os.environ.get("SMS_API_KEY")
SMS_SENDER  = os.environ.get("SMS_SENDER_ID")
```

Ensure the **order of input features** passed to the model matches the training-time column order exactly.

---

## Deployment

### Gunicorn (recommended for production)

```bash
gunicorn app:app
```

### Render

This application is live on [Render](https://render.com). To deploy your own instance:

1. Push the repository to GitHub.
2. Create a new **Web Service** on Render and connect your repository.
3. Set the **Start Command** to `gunicorn app:app`.
4. Add your SMS credentials as **environment variables** in the Render dashboard.

---

## Contributing

Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## Authors

- **Michael Osiako Afote**
- **Fati Oiza Ochepa**

---

## Citation

If you use this project or the associated research in your work, please cite:

**APA:**
> Afote, M. O., & Ochepa, F. O. (2025). Accidental Fall Prediction and Detection in Elderly Persons using Ensemble Techniques. *International Journal of Computer Applications, 186*(78), 32–36. https://doi.org/10.5120/ijca2025924684

**BibTeX:**
```bibtex
@article{10.5120/ijca2025924684,
  author    = {Michael Osiako Afote and Fati Oiza Ochepa},
  title     = {Accidental Fall Prediction and Detection in Elderly Persons using Ensemble Techniques},
  journal   = {International Journal of Computer Applications},
  volume    = {186},
  number    = {78},
  pages     = {32--36},
  month     = {April},
  year      = {2025},
  issn      = {0975-8887},
  doi       = {10.5120/ijca2025924684},
  publisher = {Foundation of Computer Science (FCS), NY, USA}
}
```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.
