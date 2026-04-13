# 📧 Spam Email Detection System using Machine Learning and Flask

A web-based machine learning application that classifies emails/messages as **Spam** or **Not Spam (Ham)** using **Natural Language Processing (NLP)** and **Flask**.

---

## 🎯 Objective
The objective of this project is to build an intelligent web application that automatically detects whether an email or SMS message is spam or genuine.

With the growing number of unwanted emails and promotional messages, manual filtering becomes inefficient. This project solves that problem by using **Machine Learning algorithms** for automated spam detection.

---

## 🧠 Problem Statement
Spam messages are unwanted and often harmful. They can include:
- Promotional scams
- Fraud links
- Fake lottery messages
- Phishing emails
- Unwanted advertisements

This project helps users instantly classify text messages into:
- **Spam**
- **Not Spam (Ham)**

using a trained ML model.

---

## 🛠️ Technologies Used
- **Python**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **HTML/CSS**
- **Pickle**
- **VS Code**

---

## 📊 Dataset
This project uses the **SMS Spam Collection Dataset**.

Dataset columns:
- `label` → spam / ham
- `message` → actual text content

Example:

| label | message |
|--------|----------|
| spam | Congratulations! You won ₹10,000 |
| ham | Hey, are we meeting today? |

---

## ⚙️ Machine Learning Workflow
The ML pipeline used in this project:

1. Data Cleaning
2. Text Preprocessing
3. Tokenization
4. Stopword Removal
5. TF-IDF Vectorization
6. Model Training
7. Pickle Model Saving
8. Flask Deployment

---

## 🤖 Model Used
The spam classifier is trained using:

- **Multinomial Naive Bayes**
- TF-IDF Vectorizer

Saved files:
- `spam_model.pkl`
- `vectorizer.pkl`

---

## 🌐 Web Application Features
✅ User-friendly UI  
✅ Real-time spam prediction  
✅ Fast response  
✅ Flask backend integration  
✅ ML model deployment  
✅ Simple and clean frontend  

---

## 📂 Project Structure
```bash
spam-ui-project/
│── app.py
│── spam_model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md
│── .gitignore
│── templates/
│   └── index.html
