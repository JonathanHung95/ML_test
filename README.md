# ML_test

Testing out deploying a simple ML model to the cloud via Docker.

### Model

We use a loan dataset found here, https://www.kaggle.com/burak3ergun/loan-data-set , to build a Logistic Regression model using most of the features.  Data preprocessing can be found under the model.py file.

### Web App

We use Flask to build a simple web UI where feature details can be input and where they will be processed into a format necessary for the model to make predictions with.  Below is an example of the calculator in action:

![Loan Calculator](assets/calculator.png)

Waitress serves as our WSGI server.  Details can be found under the app.py file.

### Docker

Docker is used to package the model and Flask app for deployment to a cloud environment.  Details can be found in the Dockerfile.