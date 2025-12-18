from flask import Flask, request, render_template
import pandas as pd
import pickle
import shap
# Load trained pipeline
with open("models/bank_marketing_model.pkl", "rb") as f:
    model = pickle.load(f)


preprocess=model.named_steps['preprocess']#Extracting the prerocess steps from the pipeline for building shap
xgb_model=model.named_steps['model']#Extracting the model steps from the pipeline for building shap
explainer=shap.TreeExplainer(xgb_model)
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_form", methods=["POST"])
def predict_form():

    input_data = {
        "age": int(request.form["age"]),
        "job": request.form["job"],
        "marital": request.form["marital"],
        "education": request.form["education"],
        "default": request.form["default"],
        "balance": float(request.form["balance"]),
        "housing": request.form["housing"],
        "loan": request.form["loan"],
        "contact": request.form["contact"],
        "day": int(request.form["day"]),
        "month": request.form["month"],
        "campaign": int(request.form["campaign"]),
        "pdays": int(request.form["pdays"]),
        "previous": int(request.form["previous"]),
        "poutcome": request.form["poutcome"]
    }

    input_df = pd.DataFrame([input_data])

    prob = model.predict_proba(input_df)[0][1] #using the model predciting the probablity of output variable
    threshold = 0.35 #its the better threshold by considering the recall value of the model 
    prediction = "YES" if prob >= threshold else "NO"

    input_transformed = preprocess.transform(input_df)# undergoing preprocess on input data
    shap_values=explainer.shap_values(input_transformed)#processed data will pass to shap to explain why the model predict yes or no
    shap_features=shap_values[0]

    feature_names=preprocess.get_feature_names_out()# trying to get the featires names so as to plot in the grapgh of shap
    shap_contrib=dict(zip(feature_names,shap_features))
    sorted_shap=sorted(shap_contrib.items(),key=lambda x: abs(x[1]),reverse=True)[:5]

    explanations=[]
    for feature,value in sorted_shap:
        direction='increased' if value>0 else 'decreased'
        explanations.append(f"The feature '{feature}' {direction} the prediction by {abs(value):.4f}.")
    return render_template(
        "index.html",
        prediction=prediction,
        probability=round(prob, 4),
        explanations=explanations
    )

if __name__ == "__main__":
    app.run(debug=True)
