# -*- coding: utf-8 -*-
"""
Created on Thu May 18 13:01:49 2023

@author: Fatima
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# loading the models:
#model-1
heart_model= pickle.load(open('heart_disease_.sav','rb'))
#model-2



# Loading Image using PIL
im = Image.open('facee.png')
# Adding Image to web app
st.set_page_config(page_title="Medical Prediction App", page_icon = im)

# siderbar-
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', #main
                           
                           ['Home','Heart Disease Prediction'], #pages 
                       	
                           icons= ['house-heart','heart-pulse'], #icons
                           
                           default_index= 0) #=0? starting with the one with index 0

    

    
#Heart disease page:
if(selected == 'Home'):
    

    #page title 
    st.title('Welcome To Our Medical Prediction Web App! :stethoscope:')
    
    st.divider()
        
    st.subheader('This is a dedicated web application to deploy different medical models with artificial intelligence. ')
    st.markdown('**:red[It includes AI concepts such as:]**')
    st.markdown(' 1 - _Machine Learning_')
    st.markdown(' 2 - _Image Processing_')
    st.subheader('More ...?')
    
    
    
    
    


if(selected == 'Heart Disease Prediction'):
    
    #page title 
    st.title('Heart Disease Prediction Using ML')
    

    
    #1
    age = st.slider('How old are you?', 0, 100, 21)
    st.write(age, 'years old')
    
    #2
    sex = st.radio(
    "Gender of the patient",
    ('Male', 'Female'),horizontal=True)
    
    
    #trans-
    if (sex=='Male'):
        sex=0
    else:
        sex=1
    
    #3
    chest_pain_type = st.radio(
    "Chest pain type",
    ('Typical', 'Typical angina', 'Non-anginal pain', 'Asymptomatic'),horizontal=True)
    
    #trans-
    if (chest_pain_type=='Typical'):
        chest_pain_type=0
    elif (chest_pain_type=='Typical angina'):
        chest_pain_type=1
    elif (chest_pain_type=='Non-anginal pain'):
        chest_pain_type=2
    else:
        chest_pain_type=3

    
    
    #4
    resting_bp_s = st.text_input('The level of the blood pressure at resting mode in mm/HG')
    
    #5
    cholesterol = st.slider('The serum cholesterol [mm/dl]', 120, 600, 335)  
    st.write(cholesterol, ' mm/dl ')
    
    #6
    fasting_blood_sugar = st.radio(
    " Fasting blood sugar greater than 120 mg/dl?",
    ('No', 'Yes'),horizontal=True)
    
    #trans-
    if (fasting_blood_sugar=='No'):
        fasting_blood_sugar=0
    else:
        fasting_blood_sugar=1
    
    #7
    resting_ecg = st.selectbox(
    'The result of electrocardiogram at rest',
    ('Normal', 'ST', 'LVH-Left Ventricular Hypertrophy'))
    
    #trans-
    if (resting_ecg=='Normal'):
        resting_ecg=0
    elif (resting_ecg=='ST'):
        resting_ecg=1
    else:
        resting_ecg=2
    
    #8
    max_heart_rate = st.slider('The maximum heart rate achieved', 60, 202, 131)  
    st.write(max_heart_rate, 'Maximum heart rate')
    
    
    #9
    exercise_angina = st.radio(
    "Exercise angina",
    ('No', 'Yes'),horizontal=True)
    
    #trans-
    if (exercise_angina=='No'):
        exercise_angina=0
    else:
        exercise_angina=1
    
    #10
    oldpeak = st.number_input('ST [Numeric value measured in depression]')
    st.write('ST segment ', oldpeak)
    
    #11
    ST_slope = st.radio(
    "The slope of the peak exercise ST segment",
    ('Normal', 'Upsloping', 'Flat', 'Downsloping'),horizontal=True)
    
    #trans-
    if (ST_slope=='Normal'):
        ST_slope=0
    elif (ST_slope=='Upsloping'):
        ST_slope=1
    elif (ST_slope=='Flat'):
        ST_slope=2
    else:
        ST_slope=3
    
      
    
    #code of pred
    
    heart_di= '' #empty str
    
    #button for pred
    
    #-image
    
    image = Image.open('clear_heart.png')
    new_image = image.resize((400, 400))
    left_co, cent_co,last_co = st.columns(3)
    with last_co:
        st.image(new_image)
    
    with cent_co:
        if st.button('Heart Disease Test Result'):
            heart_pred = heart_model.predict([[age, sex, chest_pain_type, resting_bp_s, cholesterol ,fasting_blood_sugar, resting_ecg , max_heart_rate, exercise_angina, oldpeak, ST_slope]])
            
            if (heart_pred[0]==1):
                heart_di= 'This patient could be suffering from heart disease '
            else:
                heart_di = 'This patient might not be suffering from heart disease '     
        st.success(heart_di)


    
    
    
        
    #continue the rest down here
