# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:32:47 2023

@author: sifta
"""

import numpy as np
import pickle  #loading the saved model
import streamlit as st  #creating the web page


#loading the saved model

loaded_model=pickle.load(open('trained_model.sav','rb'))

#Creating a function for prediction
def diabetes_predictoin(input_data):
    
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshape= input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)

    if(prediction[0]==0):
        return'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    
    #Giving a title
    st.title('Diabetes Prediction Web App')
    
    #Getting the input data from the user.
    #Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('Blood Pressure value')
    SkinThickness=st.text_input('Skin Thickness Value')
    Insulin=st.text_input('Insulin Level')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    Age=st.text_input('Age of the Person')
    
    
    #Code for Prediction 
    
    diagnosis=''  #Final Result will be stored.
    
    #Creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_predictoin([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
          
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    
    
