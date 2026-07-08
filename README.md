# PHEA-ATLAS AI

> Physics-Informed Machine Learning Framework for High Entropy Alloy Phase Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-green)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Live Demo

🌐 https://phea-atlas-ai.onrender.com

---

## Overview

PHEA-ATLAS AI is a Physics-Informed Machine Learning framework developed for predicting the probability of Single Phase formation in High Entropy Alloys (HEAs).

The model combines metallurgical equations with an XGBoost machine learning model to deliver fast and reliable predictions through a web interface.

---

## Features

- Physics-informed Feature Engineering
- XGBoost Prediction Model
- Automatic PDF Report Generation
- Web-based User Interface
- Scientific Alloy Calculations
- Cloud Deployment using Render

---

## Physics Features

- ΔHmix
- δ (Atomic Size Difference)
- Ω
- Λ
- VEC
- Mixing Entropy
- Mean Atomic Radius
- Mean Density
- Mean Melting Point

---

## Technologies

- Python
- Flask
- XGBoost
- NumPy
- Pandas
- Scikit-learn
- HTML
- CSS
- JavaScript
- ReportLab

---

## Project Structure

```text
PHEA-ATLAS-AI
│
├── app.py
├── predictor.py
├── feature_calculator.py
├── models/
├── data/
├── templates/
├── static/
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/dip143218/PHEA-ATLAS-AI.git

cd PHEA-ATLAS-AI

pip install -r requirements.txt

python app.py
```

## Author

**Morsalin Hossain Dip**

Department of Materials and Metallurgical Engineering

Chittagong University of Engineering & Technology (CUET)

Bangladesh

## License

This project is licensed under the MIT License.
