import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="HealthSphere : Personalized Health Assistant",
                   layout="wide",
                   page_icon="⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Diabetes Prediction Using Machine Learning',
                           ['Diabetes Prediction',
                            'Exercise Suggestion'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'exercise'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

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


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Exercise suggestions dataset
exercises = {
    'Diabetes': "1. Walking\n2. Cycling\n3. Swimming\n4. Aerobic exercises",
    'Heart Disease': "1. Walking\n2. Jogging\n3. Cycling\n4. Light weight training",
    'Parkinson\'s': "1. Stretching\n2. Dancing\n3. Yoga\n4. Balance exercises",
    'Hypertension': "1. Brisk walking\n2. Cycling\n3. Swimming\n4. Yoga",
    'Asthma': "1. Walking\n2. Yoga\n3. Swimming (in warm water)\n4. Breathing exercises",
    'Osteoporosis': "1. Weight-bearing exercises\n2. Resistance training\n3. Tai Chi\n4. Dancing",
    'Arthritis': "1. Low-impact aerobic exercises\n2. Strength training\n3. Swimming\n4. Stretching",
    'Back Pain': "1. Walking\n2. Stretching\n3. Core strengthening\n4. Yoga",
    'Depression': "1. Aerobic exercises\n2. Yoga\n3. Dance\n4. Hiking",
    'Anxiety': "1. Yoga\n2. Tai Chi\n3. Walking\n4. Pilates",
    'Chronic Fatigue Syndrome': "1. Low-impact aerobics\n2. Stretching\n3. Swimming\n4. Walking",
    'Fibromyalgia': "1. Gentle aerobic exercises\n2. Stretching\n3. Yoga\n4. Water aerobics",
    'Multiple Sclerosis': "1. Stretching\n2. Walking\n3. Swimming\n4. Balance exercises",
    'COPD': "1. Walking\n2. Breathing exercises\n3. Cycling\n4. Swimming",
    'Obesity': "1. Walking\n2. Swimming\n3. Cycling\n4. Aerobic exercises",
    'Kidney Disease': "1. Walking\n2. Yoga\n3. Cycling (low intensity)\n4. Stretching",
    'Liver Disease': "1. Walking\n2. Light aerobics\n3. Cycling\n4. Yoga",
    'Cancer': "1. Walking\n2. Yoga\n3. Tai Chi\n4. Stretching",
    'Epilepsy': "1. Low-impact aerobics\n2. Yoga\n3. Walking\n4. Swimming",
    'Dementia': "1. Walking\n2. Dancing\n3. Gardening\n4. Balance exercises",
    'Allergies': "1. Walking\n2. Cycling\n3. Swimming\n4. Stretching",
    'Scleroderma': "1. Range-of-motion exercises\n2. Swimming\n3. Stretching\n4. Tai Chi",
    'Celiac Disease': "1. Walking\n2. Yoga\n3. Swimming\n4. Light resistance training",
    'Gout': "1. Low-impact aerobics\n2. Swimming\n3. Walking\n4. Stretching",
    'Bipolar Disorder': "1. Aerobic exercises\n2. Yoga\n3. Walking\n4. Dance",
    'PTSD': "1. Yoga\n2. Walking\n3. Tai Chi\n4. Mindfulness meditation",
    'Hyperthyroidism': "1. Light aerobic exercises\n2. Stretching\n3. Yoga\n4. Walking",
    'Hypothyroidism': "1. Walking\n2. Resistance training\n3. Yoga\n4. Swimming",
    'Pneumonia': "1. Breathing exercises\n2. Walking (as tolerated)\n3. Stretching\n4. Light aerobics",
    'Sickle Cell Disease': "1. Low-impact aerobics\n2. Swimming\n3. Walking\n4. Stretching",
    'Insomnia': "1. Yoga\n2. Walking\n3. Relaxation techniques\n4. Breathing exercises",
    'Vertigo': "1. Balance exercises\n2. Tai Chi\n3. Walking\n4. Yoga",
    'Carpal Tunnel Syndrome': "1. Wrist stretches\n2. Hand strengthening\n3. Yoga\n4. Swimming",
    'Tendonitis': "1. Stretching\n2. Strength training\n3. Low-impact aerobics\n4. Swimming",
    'Plantar Fasciitis': "1. Stretching\n2. Low-impact aerobics\n3. Swimming\n4. Walking",
    'Menopause': "1. Walking\n2. Yoga\n3. Aerobic exercises\n4. Strength training",
    'Pregnancy': "1. Walking\n2. Swimming\n3. Prenatal yoga\n4. Light strength training",
    'Acid Reflux': "1. Walking\n2. Yoga\n3. Stretching\n4. Low-impact aerobics",
    'Irritable Bowel Syndrome': "1. Yoga\n2. Walking\n3. Tai Chi\n4. Swimming",
    'Schizophrenia': "1. Walking\n2. Yoga\n3. Aerobic exercises\n4. Mindfulness",
    'HIV/AIDS': "1. Walking\n2. Yoga\n3. Stretching\n4. Low-impact aerobics",
    'Psoriasis': "1. Swimming\n2. Yoga\n3. Walking\n4. Stretching",
    'Ulcerative Colitis': "1. Walking\n2. Yoga\n3. Light aerobics\n4. Swimming",
    'Lyme Disease': "1. Gentle yoga\n2. Walking\n3. Swimming\n4. Tai Chi",
    'Cushing\'s Syndrome': "1. Light aerobic exercises\n2. Yoga\n3. Walking\n4. Stretching",
    'Addison\'s Disease': "1. Gentle yoga\n2. Walking\n3. Stretching\n4. Low-impact aerobics",
    'Thyroid Cancer': "1. Walking\n2. Light resistance training\n3. Yoga\n4. Swimming",
    'Aortic Aneurysm': "1. Light walking\n2. Swimming (gentle)\n3. Stretching\n4. Yoga",
    'Chronic Sinusitis': "1. Breathing exercises\n2. Yoga\n3. Walking\n4. Stretching",
    'Raynaud\'s Disease': "1. Gentle exercises (indoors)\n2. Swimming\n3. Stretching\n4. Yoga",
    'Rheumatoid Arthritis': "1. Swimming\n2. Low-impact aerobics\n3. Stretching\n4. Tai Chi",
}

# Modify the chatbot section in your existing Streamlit code
if selected == 'Exercise Suggestion':
    st.title('Exercise Suggestion Chatbot')

    # Input for disease
    disease_input = st.text_input('Enter your disease (e.g., Diabetes, Heart Disease, Parkinson\'s):')

    # Button to get exercise suggestion
    if st.button('Get Exercise Suggestion'):
        if disease_input:
            suggestion = exercises.get(disease_input, "Sorry, I don't have suggestions for that disease.")
            st.success(f"Suggested exercises for {disease_input}:\n{suggestion}")
        else:
            st.warning("Please enter a disease to get exercise suggestions.")

