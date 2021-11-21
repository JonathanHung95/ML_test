from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from waitress import serve
import warnings

def process_features(feature_list):
    """
    Function to process data into the format needed for making predictions.

    feature_list -> List of features retrieved from the from.
    return -> List of transformed features needed for the model to make a prediction.
    """
    # feature_list: [dependents, applicant_income, coapplicant_income, loan_amt, loan_amt_term, gender, married, education, self_employed, credit_history, property]

    dependents = int(feature_list[0])
    applicant_income = int(feature_list[1])
    coapplicant_income = int(feature_list[2])
    loan_amt = int(feature_list[3])
    loan_amt_term = int(feature_list[4])
    gender_male = 1 if feature_list[5] == "male" else 0
    married_yes = 1 if feature_list[6] == "yes" else 0
    education_not_graduate = 1 if feature_list[7] == "graduate" else 0
    self_employed_yes = 1 if feature_list[8] == "yes" else 0
    credit_history = 1 if feature_list[9] == "yes" else 0
    property_area_urban = 1 if feature_list[10] == "urban" else 0
    property_area_semiurban = 1 if feature_list[10] == "semi_urban" else 0

    return [dependents, applicant_income, coapplicant_income, loan_amt, loan_amt_term, gender_male, married_yes, education_not_graduate,
                self_employed_yes, credit_history, property_area_urban, property_area_semiurban]

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
warnings.filterwarnings("ignore")

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    features = [x for x in request.form.values()]
    processed_features = [np.array(process_features(features))]

    prediction = model.predict(processed_features)
    output = "Loan Approved!" if prediction[0] == "Y" else "Loan Denied!"

    return render_template("form.html", loan_status = output)





if __name__ == "__main__":
    #app.run(debug = True, host = "0.0.0.0")
    serve(app, host = "0.0.0.0", port = 5050, threads = 2)