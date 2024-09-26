import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration 
st.set_page_config(page_title='Health Guard',layout='wide')

#path ofworking directory

working_dir=os.path.dirname(os.path.abspath(__file__))


# loading of the saved models
diabetes_model= pickle.load(open('diabetes_madel.sav','rb'))
heart_disease_model= pickle.load(open('heart_model.sav','rb'))


#sidebar for navigation 

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Predication','Heart Disease Prediction'],menu_icon='hospital-fill',icons=['activity','heart'],default_index=0)
# ,'Parkinsons Prediction',,,,'person'
# diabetes predication page

if selected =='Diabetes Predication':
    # page title
    st.title('Diabetes Prediction using ML ')
    
    # getting the input data from the user

    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies ')
    with col2:

        glucode = st.text_input('Glucose Level')
    with col3:
        bloodpressure = st.text_input('Blood Pressure Value')

    with col1:
        skinthickness = st.text_input('Skin Thickness value')
    with col2:
        insuline = st.text_input('Insuline Level')
    with col3:
        bmi = st.text_input('BMi Value')
    with col1:
        dpf = st.text_input('Diabetes Pedigree function value')
    with col2:
        age = st.text_input('Age of the Function ')
    
    #backend logic
    diab_diagnosis =''

    # creation of a button
    if st.button('Diabetes Test Result'):
        input = [Pregnancies,glucode,bloodpressure,skinthickness,insuline,bmi,dpf,age]

        input = [float(x) for x in input]

        diab_prediction = diabetes_model.predict([input])
        
        if diab_prediction[0] ==1:
            diab_diagnosis = 'The Person is diabetic '
        else:
            diab_diagnosis = 'The Person is not diabetic'
    st.success(diab_diagnosis)

# heart ============================================

if selected =='Heart Disease Prediction':
    # page title
    st.title('Heart Prediction using ML ')
    
    # getting the input data from the user

    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age ')
    with col2:

        gender = st.text_input('Gender')
    with col3:
        cp = st.text_input('Chesr Pain Type')

    with col1:
        tresttyps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Chlestorel in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results ')
    with col2:
        mhra = st.text_input('Miaximum heart rate achieved ')
    with col3:
        ela = st.text_input('Exercise Induced Angine ')
    
    with col1:
        oldpeak = st.text_input('St depression induced by exercise ')
    with col2:
        slop = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        mcf = st.text_input('Major vessels colored by flourosopy')
    
    with col1:
        thal = st.text_input('thal:0 =  normal;1= fixed defect; 2=reversable defect')
    
    
    #backend logic
    heart_diagnosis =''

    # creation of a button
    if st.button('Diabetes Test Result'):
        input = [age,gender,cp,tresttyps,chol,fbs,restecg,mhra,ela,oldpeak,slop,mcf,thal]

        input = [float(x) for x in input]

        heart_diagnosis = heart_disease_model([input])
        
        if heart_diagnosis[0] ==1:
            heart_diagnosis = 'The Person is diabetic '
        else:
            heart_diagnosis = 'The Person is not diabetic'
    st.success(heart_diagnosis)