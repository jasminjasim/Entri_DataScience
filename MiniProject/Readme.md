# Bank Marketing Prediction – Mini Project

This project predicts whether a bank customer will subscribe to a term deposit using
machine learning models trained on the UCI Bank Marketing dataset.

The solution includes data preprocessing, handling class imbalance, model training,
evaluation, and explainability using SHAP.

---

## Dataset
- **Source**: UCI Bank Marketing Dataset (`bank-full.csv`)
- **Target Variable**: `y`
  - `yes` → 1 (Subscribed)
  - `no` → 0 (Not Subscribed)

---

## Key Preprocessing Steps

### 1. Handling Missing Values & Outliers
- No missing values found.
- Outliers observed mainly in the `balance` column.
- Since this is financial data, outliers were **not removed** as they represent real customer behavior.

### 2. Feature Selection
- The `duration` feature was **removed** to avoid data leakage.
  - Call duration is only known **after** the call is completed.
  - Including it would result in an unrealistically high model performance.

### 3. Feature Encoding & Scaling
- **Categorical Features**:
  - OneHotEncoding (`job`, `marital`, `education`, `default`, `housing`, `loan`, `contact`, `month`, `poutcome`)
- **Numerical Features**:
  - RobustScaler (XGBoost)
  - StandardScaler (SVM)

### 4. Class Imbalance Handling
- The dataset is imbalanced (more “no” than “yes”).
- **SMOTE (Synthetic Minority Oversampling Technique)** was applied within the training pipeline.

---

## Models Used

### 1. XGBoost Classifier
- RobustScaler for numerical features
- OneHotEncoding for categorical features
- SMOTE for imbalance handling
- Evaluation metric: `logloss`

### 2. Support Vector Machine (SVM)
- StandardScaler for numerical features
- OneHotEncoding for categorical features
- SMOTE applied before training
- RBF kernel with probability estimation enabled

---

## Model Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC Score

Both models were evaluated on a stratified train-test split (80% train, 20% test).

---

## Model Explainability
- **SHAP (SHapley Additive exPlanations)** is used for interpretability.
- Tree-based SHAP Explainer is applied to the XGBoost model.
- SHAP summary plots show:
  - Feature importance
  - Direction of impact on predictions

---

## Saved Model
- The trained XGBoost pipeline (including preprocessing and SMOTE) is saved as:
models/bank_marketing_model.pkl

## Accuracy
Classification Report for XGboost:
               precision    recall  f1-score   support

           0       0.91      0.97      0.94      7985
           1       0.59      0.29      0.39      1058

    accuracy                           0.89      9043
   macro avg       0.75      0.63      0.67      9043
weighted avg       0.87      0.89      0.88      9043

Confusion Matrix for XGboost:
 [[7777  208]
 [ 753  305]]
Accuracy Score for XGboost:
 0.8937299568727193
Classification Report for SVC:
               precision    recall  f1-score   support

           0       0.94      0.88      0.91      7985
           1       0.37      0.55      0.44      1058

    accuracy                           0.84      9043
   macro avg       0.65      0.71      0.67      9043
weighted avg       0.87      0.84      0.85      9043

Confusion Matrix for SVC:
 [[7010  975]
 [ 480  578]]
Accuracy Score for SVC:
 0.8391020678978215
ROC-AUC Score: 0.7847165585756848
ROC-AUC Score for SVC: 0.7746648666627999

## Screenshot
<img width="332" height="688" alt="image" src="https://github.com/user-attachments/assets/23204ae3-ebb2-45e3-9953-9d02fa0ed3a7" />

