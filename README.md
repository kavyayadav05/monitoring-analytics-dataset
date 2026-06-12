# Monitoring Analytics Dataset Generator

## 📌 Objective
Prepare monitoring dataset for analytics dashboards and reporting.

## 📊 Dataset Fields
- candidate_id
- risk_score
- phone_events
- session_duration

## ⚙️ Features
- Generates synthetic monitoring data
- Handles missing values
- Removes duplicate candidates
- Validates all fields

## 📁 Project Structure
- data/ → dataset.csv
- src/ → dataset generator script
- notebook/ → analytics notebook
- data_dictionary.md → column explanation

## ▶️ How to Run
python src/generate_dataset.py

## 📈 Analytics
Use notebook/analysis.ipynb for:
- Data analysis
- Risk distribution
- High-risk detection

## ✅ Status
✔ Dataset ready  
✔ Validated data  
✔ Dashboard-ready