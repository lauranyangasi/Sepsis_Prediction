# Sepsis_Prediction
A Machine Learning Journey from Development to Deployment
## Introduction
Sepsis is a life-threatening medical condition that demands swift intervention. In this article, we explore the development of a machine learning model for predicting sepsis and deploy it as a FastAPI web API using Docker. This journey involves understanding the problem, exploring the data, building a model, and making it accessible through a web interface.

## Business Understanding
Sepsis occurs when the body's response to an infection becomes excessive, leading to organ failure. Intensive Care Units (ICUs) closely monitor patients for sepsis development. Our goal is to build a machine learning model that predicts whether a patient in the ICU will develop sepsis, facilitating early intervention.

## Analytical Questions and Data Understanding
We begin by formulating hypotheses and asking analytical questions such as the distribution of sepsis cases, correlation of different features with sepsis, and the impact of age. The dataset is explored using Python libraries, and features like Plasma Glucose, Blood Work Results, and Age are identified as key factors.

## Exploratory Data Analysis (EDA)
EDA involves statistical analysis and visualization of the dataset. Box plots and histograms highlight the differences in health features between patients with positive and negative sepsis status. This exploration guides our understanding of the data and informs preprocessing decisions.

## Data Cleaning and Preprocessing
To prepare the data for machine learning, we drop unnecessary columns, rename misspelled ones, and encode the target variable. Privacy concerns lead to the removal of patient IDs, insurance information, and encoding the Sepsis column into binary form (1 for Positive, 0 for Negative).

## Machine Learning Model Development
We address class imbalance in the target variable through upsampling and split the data into training and testing sets. Three classifiers – K-Nearest Neighbors, XGBoost, and Decision Tree – are implemented using pipelines. The XGBoost model, showing promising results, is selected for further use.

## Model Deployment with FastAPI and Docker
Now, we move from model development to deployment. FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints, is employed. Docker is used for containerization.

## The FastAPI Web API
We create an API endpoint /predict_sepsis that accepts patient features (PRG, PL, PR, SK, TS, M11, BD2, Age) as input. The deployed model makes predictions, and the result is sent back as a response. The API is hosted, and users can interact with it through HTTP requests.

## Conclusion
Predicting sepsis involves a holistic approach, from understanding the medical problem to deploying a machine learning model as a web API. FastAPI and Docker simplify the deployment process, providing an accessible interface for healthcare professionals to leverage the predictive power of machine learning in identifying patients at risk of sepsis.

In conclusion, this project demonstrates the potential of combining data science, machine learning, and web development to address critical healthcare challenges.
