# Monitoring Analytics Dataset Generator

## Overview
This project creates a dataset for monitoring candidate activity.

## Data Fields
- Candidate ID
- Risk Score
- Phone Events
- Session Duration

## Project Structure
- data/dataset.csv
- notebook/analysis.ipynb
- src/generate_dataset.py
- data_dictionary.md

## Sample Data
candidate_id,risk_score,phone_events,session_duration  
101,65,2,35  
102,15,0,50  

## Features
- Handles missing values  
- Removes duplicates  
- Validated dataset  

## How to Run
1. Install pandas  
2. Run: python src/generate_dataset.py  

## Author
Kavya Yadav