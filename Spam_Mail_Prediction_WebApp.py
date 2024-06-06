# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:55:22 2024

@author: prachet
"""

import numpy as np
import pickle
import streamlit as st

with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

with open("feature_extraction.pkl", 'rb') as f:
    feature_extraction = pickle.load(f)
    
#creating a function for prediction

def spam_mail_prediction(input_data):

    #convert text to feature vectors
    input_data_features = feature_extraction.transform(input_data)
    
    #making prediction
    prediction = model.predict(input_data_features)
    print(prediction)
    
    if(prediction[0]==0):
      return "Spam Mail"
    else:
      return "Ham Mail"
  
def main():
    
    #giving a title
    st.title('Spam Mail Prediction Web App')
    
    #getting input data from user
    
    mail = st.text_input("Enter Mail Here")
    
    # code for prediction
    pred = ''
    
    #creating a button for Prediction
    if st.button('Predict Mail'):
        pred = spam_mail_prediction([mail])
        
    st.success(pred)
    
    
    
if __name__ == '__main__':
    main()    


