import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.impute import KNNImputer
import pickle

if __name__ == "__main__":
    loans = pd.read_csv("data/loan_data_set.csv")

    # handle some of the missing variables with mode imputation

    loans["Gender"].fillna(loans["Gender"].mode()[0], inplace = True)
    loans["Married"].fillna(loans["Married"].mode()[0], inplace = True)
    loans["Dependents"].fillna(loans["Dependents"].mode()[0], inplace = True)
    loans["Self_Employed"].fillna(loans["Self_Employed"].mode()[0], inplace = True)
    loans["Credit_History"].fillna(loans["Credit_History"].mode()[0], inplace = True)

    # one hot encode for modelling + set up for KNN imputation of LoanAmount and Loan_Amount_Term

    loans = pd.get_dummies(loans, 
                        columns = ["Gender", "Married", "Education", "Self_Employed", "Credit_History", "Property_Area"], 
                        drop_first = True)

    # handle 3+ dependents by converting to 3

    loans["Dependents"].replace("3+", 3, inplace = True)

    # KNN Imputation 

    imputer = KNNImputer(n_neighbors = 1)
    loans["Loan_Amount_Term"] = imputer.fit_transform(loans[["Loan_Amount_Term"]]).ravel()

    imputer = KNNImputer(n_neighbors = 3)
    loans["LoanAmount"] = imputer.fit_transform(loans[["LoanAmount"]]).ravel()

    # create logistic regression model

    X = loans[["Dependents", "ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", 
                "Gender_Male", "Married_Yes", "Education_Not Graduate", "Self_Employed_Yes", "Credit_History_1.0",
                "Property_Area_Semiurban", "Property_Area_Urban"]]

    y = loans["Loan_Status"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 88)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    pickle.dump(model, open("model.pkl", "wb"))

