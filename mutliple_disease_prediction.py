# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:35:28 2024

@author: sujal
"""

import pickle
import requests
import streamlit as st
from streamlit_option_menu import option_menu

#loading the models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))


# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple disease prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],icons=['clipboard2-pulse','clipboard-heart','activity'],default_index=0)

if(selected == 'Diabetes Prediction'):
    st.title('Diabetes prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
   
    with col2:
       Insulin = st.text_input('Insulin Level')
       
    with col3:
       BMI = st.text_input('BMI value')
      
    with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
   
    with col2:
       Age = st.text_input('Age of the Person')
      
   
    
    diab_diag = ' '
    
    if st.button('Test Result'):
        diab_pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_pred[0]==1):
            diab_diag = 'The Person is Diabetic'
            st.success(diab_diag)
            st.header("Remedies for Diabetes")

           
            st.write("Limit sugar intake.")
            st.write("Choose complex carbohydrates over refined ones.")
            st.write("Control portion sizes.")
            st.write("Limit sugar intake:")
            sugar_limit = st.slider("Daily sugar intake (grams)", min_value=0, max_value=100, value=50)
            exercise_duration = st.slider("Target exercise duration (minutes/day)", min_value=0, max_value=120, value=30)

             
            
        



            
        else:
            diab_diag = 'The Person is not Diabetic'
            st.success(diab_diag)
            
  
    
     
    
if(selected == 'Heart Disease Prediction'):
    st.title('heart disease prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input('age of a person')

        try:
         age = int(age) 
        except ValueError:
         age = None  # Or handle the error as needed
    
    with col2:
        sex = st.text_input('sex (1-M,0-F)')
        try:
         sex = int(sex) 
        except ValueError:
         sex = None  # Or handle the error as needed
        
    with col3:
        cp = st.text_input('constrictive pericarditis')
        try:
         cp = int(cp) 
        except ValueError:
         cp = None 
        
    with col1:
       trestbps = st.text_input('trest bps value')
       try:
        trestbps = int(trestbps) 
       except ValueError:
        trestbps = None 
    with col2:
       chol = st.text_input('cholestrol value')
       try:
        chol = int(chol) 
       except ValueError:
        chol = None 
    with col3:
       fbs = st.text_input('fbs value')
       try:
        fbs = int(fbs) 
       except ValueError:
        fbs = None 
    with col1:
       restecg = st.text_input('restecg')
       try:
        restecg= int(restecg) 
       except ValueError:
        restecg = None 
    with col2:
       thalach = st.text_input('thalach')
       try:
        thalach = int(thalach) 
       except ValueError:
        thalach = None 
    with col3:
        exang = st.text_input('exang')
        try:
         exang = int(exang) 
        except ValueError:
         exang = None 
    with col1:
        oldpeak = st.text_input('oldpeak')
        try:
         oldpeak = float(oldpeak) 
        except ValueError:
         oldpeak = None 
    with col2:
        slope = st.text_input('slope')
        try:
         slope = int(slope) 
        except ValueError:
         slope = None 
    with col3:
        ca = st.text_input('ca')
        try:
         ca = int(ca) 
        except ValueError:
         ca = None 
    with col2:
        thal = st.text_input('thal')
        try:
         thal = int(thal) 
        except ValueError:
         thal = None 
      
   
    
    heart_diag = ' '
    
    if st.button('Test Result'):
        heart_pred = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_pred[0]==1):
            heart_diag = 'You have heart disease'
            
        else:
            heart_diag = 'You don\'t have heart disease'
    st.success(heart_diag)
    
    
    
    
if(selected == 'Parkinsons Prediction'):
    st.title('parkinsons prediction using ML')
    
    
    
    Fo = st.text_input('Fo(Hz)')
    Fhi = st.text_input('Fhi(Hz)')
    Flo = st.text_input('Flo(Hz)')
    Jitter = st.text_input('Jitter(%)')
    JitterAbs = st.text_input('Jitter(Abs)')
    RAP = st.text_input('RAP')
    PPQ = st.text_input('PPQ')
    DDP = st.text_input('DDP')
    Shimmer = st.text_input('Shimmer')
    ShimmerdB = st.text_input('Shimmer(dB')
    ShimmeAPQ3 = st.text_input('APQ3')
    ShimmerAPQ5 = st.text_input('APQ5')
    APQ = st.text_input('APQ')
    ShimmerDDA = st.text_input('DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    status = st.text_input('status')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')
    
    
    
    
    parkinson_diag = ' '
    
    if st.button('Test Result'):
        parkinson_pred = parkinsons_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(parkinson_pred[0]==1):
            parkinson_diag = 'You have parkinson disease'
            
        else:
            parkinson_diag = 'You don\'t have parkinson disease'
    st.success(parkinson_diag)

    
    
    
    
