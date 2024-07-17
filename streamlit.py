import streamlit as st
import joblib
import numpy as np

# Charger le modèle
model_path = 'logistic_regression_model.pkl'
model = joblib.load(model_path)

# Définir les catégories pour les inputs
sex_options = ['Male', 'Female']
age_options = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older']
race_options = ['White', 'Black', 'Asian', 'Other']
genhealth_options = ['Poor', 'Fair', 'Good', 'Very good', 'Excellent']

# Titre de l'application
st.title('Prédiction de maladie')

# Entrées utilisateur
bmi = st.slider('BMI', 10, 50, 25)
smoking = st.radio('Smoking', [0, 1])
alcohol_drinking = st.radio('Alcohol Drinking', [0, 1])
stroke = st.radio('Stroke', [0, 1])
physical_health = st.slider('Physical Health', 0, 30, 15)
mental_health = st.slider('Mental Health', 0, 30, 15)
diff_walking = st.radio('Difficulty Walking', [0, 1])
sex = st.selectbox('Sex', sex_options)
age_category = st.selectbox('Age Category', age_options)
race = st.selectbox('Race', race_options)
diabetic = st.radio('Diabetic', [0, 1])
physical_activity = st.radio('Physical Activity', [0, 1])
gen_health = st.selectbox('General Health', genhealth_options)
sleep_time = st.slider('Sleep Time', 0, 24, 7)
asthma = st.radio('Asthma', [0, 1])
kidney_disease = st.radio('Kidney Disease', [0, 1])
skin_cancer = st.radio('Skin Cancer', [0, 1])

# Mapping des inputs catégoriels en numériques
sex_map = {'Male': 0, 'Female': 1}
age_map = {age: idx for idx, age in enumerate(age_options)}
race_map = {race: idx for idx, race in enumerate(race_options)}
gen_health_map = {health: idx for idx, health in enumerate(genhealth_options)}

# Convertir les entrées en un tableau numpy
input_data = np.array([bmi, smoking, alcohol_drinking, stroke, physical_health, mental_health,
                       diff_walking, sex_map[sex], age_map[age_category], race_map[race], diabetic,
                       physical_activity, gen_health_map[gen_health], sleep_time, asthma,
                       kidney_disease, skin_cancer]).reshape(1, -1)

# Prédire si l'utilisateur est malade ou non
if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write("Prediction: Malade")
    else:
        st.write("Prediction: Non malade")
