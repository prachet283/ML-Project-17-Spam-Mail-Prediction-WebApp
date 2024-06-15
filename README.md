# Spam Mail Prediction Web App
This repository contains a web application that predicts whether an email is spam or not using a Logistic Regression model. The application is built with a user-friendly interface and offers real-time predictions based on the email content.

# Overview
pam emails are a major issue in digital communication, causing various problems ranging from minor annoyances to severe security threats. This project aims to develop a solution to detect spam emails effectively using machine learning techniques. The application preprocesses email text using TF-IDF vectorization and classifies it with a Logistic Regression model.

# Dataset
The dataset used for training the model consists of a collection of emails labeled as spam or not spam. The data has been preprocessed to remove noise and irrelevant information.

# Technologies
Python
Pandas
NumPy
Scikit-learn
Streamlit
Matplotlib/Seaborn

# Exploratory Data Analysis (EDA)
EDA was performed to understand the distribution of data, check for class imbalances, and visualize important features. Key steps included:

Analyzing the distribution of spam and non-spam emails.
Examining correlations and patterns in the dataset.

# Model
The Logistic Regression model was chosen for its simplicity and effectiveness in binary classification tasks. Key steps included:

Data Preprocessing: Using TF-IDF vectorizer to transform email text into numerical feature vectors.
Model Training: Training the Logistic Regression model on the transformed dataset.
Evaluation: Assessing model performance using accuracy.

# Web App
The web application is built using Streamlit, providing an interactive interface for users to input email content and get predictions.


# Usage
Open your web browser and go to https://ml-project-17-spam-mail-prediction-using-machine-learning-3w8j.streamlit.app/

Upload a text file or enter email content manually.

Click the "Predict" button to see if the email is spam or not.

# Results
The model achieves high accuracy in predicting spam emails, with key metrics as follows:

Accuracy: 96.59%
These results demonstrate the model's effectiveness in distinguishing between spam and non-spam emails.

# Conclusion
This project successfully demonstrates the use of machine learning for spam email detection. The Logistic Regression model, combined with TF-IDF vectorization, provides a reliable solution for predicting spam emails. Future improvements could include testing with larger datasets, experimenting with different models, and enhancing the web application's features.

# Contributing
Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

# Deployment
The application is deployed using Streamlit. You can access it here = https://ml-project-17-spam-mail-prediction-using-machine-learning-3w8j.streamlit.app/
