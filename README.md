# SmartHire-AI-Resume
# 💼 SmartHire - AI Resume Screening & Job Recommendation System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview

SmartHire is an end-to-end Machine Learning application that automates the resume screening process by matching candidate resumes with suitable job opportunities.

The system analyzes uploaded resumes, predicts the candidate's job domain, recommends the most relevant jobs using content-based recommendation techniques, and identifies missing skills required for target roles.

This project was developed as an Industrial Machine Learning Project using **Supervised** and **Unsupervised Learning** techniques without relying on Large Language Models (LLMs).

---

# 🚀 Features

### Resume Upload
- Upload Resume (PDF)
- Automatic Resume Text Extraction

### Resume Classification
- Predict Resume Category
- Multi-class Classification using SVM

### Job Recommendation
- TF-IDF Vectorization
- Cosine Similarity Matching
- Top-N Job Recommendations

### Skill Gap Analysis
- Detect Missing Skills
- Resume Match Score
- Skill Improvement Suggestions

### Interactive Dashboard
- Professional Streamlit UI
- Resume Score
- Interview Probability
- Interactive Charts
- Download Job Recommendations

---

# 🧠 Machine Learning Pipeline

```
Resume
      │
      ▼
Resume Parser
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Vectorization
      │
 ┌───────────────┬──────────────────┐
 ▼               ▼                  ▼
Resume       Job Matching      Skill Gap
Classifier   Recommendation    Analysis
      │
      ▼
Professional Dashboard
```

---

# 📂 Project Structure

```
SmartHire/
│
├── app/
│   ├── streamlit_app.py
│   ├── pages/
│   ├── assets/
│   └── styles/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── interim/
│
├── models/
│   ├── classifier.pkl
│   ├── job_vectorizer.pkl
│   └── job_vectors.pkl
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── parsing/
│   └── utils/
│
├── notebooks/
│
├── reports/
│
├── tests/
│
├── requirements.txt
├── run.py
├── README.md
└── LICENSE
```

---

# 📊 Datasets Used

### Resume Dataset

- Resume_25 Dataset
- 25 Resume Categories
- Used for Resume Classification

### LinkedIn Job Dataset

Contains

- Job Title
- Company
- Location
- Skills
- Description

### Naukri Job Dataset

Contains

- Company
- Skills
- Experience
- Salary
- Job Description

---

# 🛠 Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- TF-IDF
- Linear SVM
- Cosine Similarity
- XGBoost (Optional)

### Data Processing

- Pandas
- NumPy
- NLTK

### Resume Parsing

- pdfplumber
- PyPDF2

### Visualization

- Plotly
- Matplotlib

### Frontend

- Streamlit

---

# 📈 Machine Learning Models

## Resume Category Classifier

Algorithm

- Linear SVM

Input

```
Resume Text
```

Output

```
Predicted Job Category
```

Evaluation

- Accuracy
- Precision
- Recall
- F1 Score

---

## Job Recommendation Engine

Algorithm

- TF-IDF
- Cosine Similarity

Input

```
Resume
```

Output

```
Top 10 Matching Jobs
```

---

## Skill Gap Analyzer

Compares

```
Resume Skills

vs

Job Skills
```

Outputs

- Missing Skills
- Matching Skills
- Resume Score

---

# 📊 Evaluation Metrics

Classification

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Recommendation

- Precision@K

Clustering (Optional)

- Silhouette Score

Regression (Optional)

- RMSE
- MAE

---

# ▶️ Installation

Clone Repository

```bash
git clone https://github.com/<your-username>/SmartHire-ML.git
```

Move into project

```bash
cd SmartHire-ML
```

Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

Train Models

```bash
python -m src.models.classifier

python -m src.models.recommender
```

Run Streamlit

```bash
streamlit run app/streamlit_app.py
```

Open

```
http://localhost:8501
```

---


# 🎯 Future Improvements

- User Authentication
- Recruiter Dashboard
- Candidate Dashboard
- PostgreSQL Database
- Docker Support
- Cloud Deployment
- Email Notifications
- Resume Ranking
- Interview Scheduling
- AI Career Guidance

---

# 🌐 Deployment

Recommended Platforms

- Streamlit Community Cloud
- Render
- Microsoft Azure
- AWS EC2

---

# 👨‍💻 Author

**Rockxy**

Engineer | Machine Learning Developer

GitHub:
https://github.com/sneha804/SmartHire-AI-Resume

LinkedIn:
www.linkedin.com/in/sneha-potluri-88869631a

---


# ⭐ Acknowledgements

- Kaggle
- Scikit-Learn
- Streamlit
- NLTK
- LinkedIn Job Dataset
- Naukri Dataset
- Resume_25 Dataset

---

## ⭐ If you found this project useful, please consider giving it a star on GitHub!
