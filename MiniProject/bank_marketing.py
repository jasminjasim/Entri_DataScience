# Loading the Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler ,RobustScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,roc_auc_score
from xgboost import XGBClassifier
import pickle
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.compose import ColumnTransformer# for scaling and encoding via pipeline
from sklearn.pipeline import Pipeline#pipeline
from sklearn.svm import SVC
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline#pipeline for smote
#-----------------------------------------------------------------------------------
warnings.filterwarnings('ignore')
#Loading the dataset
bank_data = pd.read_csv( r'C:\Users\jasmi\Downloads\ML Classes\MiniProject\bank-full.csv')
bank_data.head()
bank_data_set2=bank_data.copy()
bank_data.info()
bank_data.describe()
# - default			has credit in default?		no
# - balance	average yearly balance	euros	no
# - housing			has housing loan?		no
# - loan		has personal loan?		no
# - contact		contact communication type (categorical: 'cellular','telephone')		yes
# - day_of_week			last contact day of the week
# - month			last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')		no
# - duration		last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.		no
# - campaign		number of contacts performed during this campaign and for this client (numeric, includes last contact)		no
# - pdays		number of days that passed by after the client was last contacted from a previous campaign (numeric; -1 means client was not previously contacted)		yes
# - previous		number of contacts performed before this campaign and for this client		no
# - poutcome		outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')		yes
# - y			has the client subscribed a term deposit?		no

#-----------------------------------------------------------------------------------
#Checking for missing values and outliers
bank_data.isnull().sum()
plt.figure(figsize=(10,6))
sns.boxplot(data=bank_data)
plt.show()
#seeing ouliers in "balance" column heavily.But its a financial data so we cant remove the outliers.we cannot able to consider banking data without outliers.So keeping this it might be a true behaviour
#-----------------------------------------------------------------------------------
#Splitting the X and y before encoding and scaling
X=bank_data.drop('y',axis=1)
y=bank_data['y'].map({'no': 0, 'yes': 1})
print(y.value_counts())
#to handle imbalanced data
neg_count=y.value_counts()[0]
pos_count=y.value_counts()[1]
print(neg_count,pos_count)
scale_pos_weight = neg_count / pos_count
print(scale_pos_weight)  
#--------------------------------------------------------------------------------------
categorical_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome'] 
num_cols = ['age', 'balance', 'day', 'campaign', 'pdays', 'previous']#removed duration column as it is not known before a call is performed
for i in categorical_cols:
    print(f'Unique values in {i}: {X[i].unique()}')
#Using ColumnTransformer for scaling and encoding via pipeline for XGBoost model
preprocessor_OHE=ColumnTransformer(transformers=[
    ('num',RobustScaler(),num_cols),
    ('cat',OneHotEncoder(handle_unknown='ignore'),categorical_cols),
    ],remainder='drop')

preprocessor_Standard=ColumnTransformer(transformers=[
    ('num',StandardScaler(),num_cols),  
    ('cat',OneHotEncoder(handle_unknown='ignore'),categorical_cols),
    ],remainder='drop') 


#--------------------------------------------------------------------------------------
#Setting up the pipeline 
# pipeline_XGBoost_model_ROHE=Pipeline(steps=[('preprocess',preprocessor_OHE),
#                             ('model',XGBClassifier(random_state=42,eval_metric='logloss',scale_pos_weight=scale_pos_weight))])
pipeline_XGBoost_model_ROHE=Pipeline(steps=[('preprocess',preprocessor_OHE),
                                            ('smote', SMOTE(random_state=42)),
                            ('model',XGBClassifier(random_state=42,eval_metric='logloss'))])

# pipeline_SVC_model_Standard=Pipeline(steps=[('preprocess',preprocessor_Standard),
#                                             ('smote', SMOTE(random_state=42)),   
#                             ('model',SVC(random_state=42,probability=True))])
pipeline_SVC_model_Standard = Pipeline(steps=[
    ('preprocess', preprocessor_Standard),
    ('smote', SMOTE(random_state=42)),
    ('svc', SVC(kernel='rbf', probability=True, random_state=42))
])
#--------------------------------------------------------------------------------------
#Splitting the train and test data
print('Splitting the data into train and test sets')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
#--------------------------------------------------------------------------------------
#Fitting the model using pipeline
print('Fitting the model using pipeline')

pipeline_XGBoost_model_ROHE.fit(X_train,y_train)
pipeline_SVC_model_Standard.fit(X_train,y_train)
#--------------------------------------------------------------------------------------
#Predicting the values
print('Predicting the values')
y_pred_ROHE=pipeline_XGBoost_model_ROHE.predict(X_test)
y_pred_Standard=pipeline_SVC_model_Standard.predict(X_test)
#--------------------------------------------------------------------------------------
#Evaluating the model
print("Classification Report for XGboost:\n",classification_report(y_test,y_pred_ROHE))
print("Confusion Matrix for XGboost:\n",confusion_matrix(y_test,y_pred_ROHE))
print("Accuracy Score for XGboost:\n",accuracy_score(y_test,y_pred_ROHE))
print("Classification Report for SVC:\n",classification_report(y_test,y_pred_Standard))
print("Confusion Matrix for SVC:\n",confusion_matrix(y_test,y_pred_Standard))
print("Accuracy Score for SVC:\n",accuracy_score(y_test,y_pred_Standard))
#--------------------------------------------------------------------------------------
y_proba = pipeline_XGBoost_model_ROHE.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_proba)
print("ROC-AUC Score:", roc_auc)

y_proba_svc = pipeline_SVC_model_Standard.predict_proba(X_test)[:, 1]
roc_auc_svc = roc_auc_score(y_test, y_proba_svc)
print("ROC-AUC Score for SVC:", roc_auc_svc)


#--------------------------------------------------------------------------------------
#Saving the model as pickle file
with open('models/bank_marketing_model.pkl', 'wb') as f:
    pickle.dump(pipeline_XGBoost_model_ROHE, f)   
#--------------------------------------------------------------------------------------
#Explainability using shap model
import shap
explainer = shap.Explainer(pipeline_XGBoost_model_ROHE.named_steps['model'])
# Calculate SHAP values
X_test_preprocessed = pipeline_XGBoost_model_ROHE.named_steps['preprocess'].transform(X_test)
shap_values = explainer(X_test_preprocessed)
# Summary plot
shap.summary_plot(shap_values, feature_names=pipeline_XGBoost_model_ROHE.named_steps['preprocess'].get_feature_names_out())
#--------------------------------------------------------------------------------------





