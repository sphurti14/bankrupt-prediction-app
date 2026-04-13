#  Bankruptcy Prevention Analytics Platform

##  Project Overview
This project is an interactive **Machine Learning + Streamlit web application** that predicts whether a company is likely to go bankrupt based on critical financial and operational risk factors.

Bankruptcy prediction is a crucial problem in finance as it impacts investors, creditors, and business stakeholders. This project models bankruptcy as a **binary classification problem**, identifying whether a firm is:

- ❌ Bankrupted  
- 🎉 Not Bankrupted  

The application provides a **user-friendly dashboard** for real-time prediction and visualization.

---

##  Features

###  Bankruptcy Prediction Engine
- Predicts bankruptcy using multiple financial risk factors  
- Built using advanced Machine Learning models  
- High accuracy classification system  

###  Interactive Dashboard
- Developed using Streamlit  
- Simple and intuitive UI  
- Real-time prediction based on user inputs  

###  Data Visualization
- Feature vs Bankruptcy analysis  
- Count plots for risk comparison  
- Interactive graph selection  

---

##  Input Features

The model uses the following features:

- Industrial Risk  
- Management Risk  
- Financial Flexibility  
- Credibility  
- Competitiveness  
- Operating Risk  

Each feature is encoded as:
- **0.0 → Low Risk**
- **0.5 → Medium Risk**
- **1.0 → High Risk**

---

##  Project Architecture

Business Understanding  
↓  
Data Collection  
↓  
Data Preprocessing & Feature Engineering  
↓  
Model Training & Evaluation  
↓  
Model Deployment (Streamlit App)  

---

##  Dataset Information

- 250 companies  
- 6 input features + 1 target variable  
- No missing values  
- Balanced dataset  
- Features are discrete (0, 0.5, 1)  

---

##  Machine Learning Models Used

Multiple classification algorithms were explored:

- Logistic Regression  
- Decision Trees  
- Random Forest  
- AdaBoost  
- Gradient Boosting  
- XGBoost  
- LightGBM  
- KNN  
- SVM  
- Neural Networks  

 Final model selected: **Artificial Neural Network (ANN)** :contentReference[oaicite:0]{index=0}  

---

##  Model Performance

- Training Accuracy: **99.18%**  
- Testing Accuracy: **98.66%**  
- High precision and recall across both classes  

Key observations:
- Balanced dataset  
- Very low misclassification  
- Strong predictive capability  

Threshold used: 0.9995045

:contentReference[oaicite:1]{index=1}  

---

## 📸 How It Works

1. Select risk levels for all features  
2. Click **Predict**  
3. Get result:
   - ❌ BANKRUPTED  
   - 🎉 NOT BANKRUPTED  
4. Explore feature-based graphs  

---

## 🛠️ Tech Stack

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- TensorFlow / Keras  
- Streamlit  
- Seaborn  
- Matplotlib  

---

## ▶️ Run Locally

```bash
git clone https://github.com/sphurti14/bankrupt-prediction-app.git
cd bankruptcy-prediction-app
pip install -r requirements.txt
streamlit run prev.py

Author

Sphurti Patil
AI & Data Science Enthusiast
