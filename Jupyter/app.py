import pickle
from sys import prefix
from matplotlib.pyplot import step
import streamlit as st

pickle_in = open('Jupyter/modelo.pkl', 'rb')
classificador = pickle.load(pickle_in)

@st.cache()

def predicao(Age,Sex,Chest_pain_type,BP,Cholesterol,FBS_over_120,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope_of_depression,Number_of_vessels_fluro,Thallium):
    if Sex == "Male":
        Sex = 1
    else:
        Sex = 0

    predicao = classificador.predict([[Age,Sex,Chest_pain_type,BP,Cholesterol,FBS_over_120,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope_of_depression,Number_of_vessels_fluro,Thallium]])        
    pred0 = classificador.predict_proba([[Age,Sex,Chest_pain_type,BP,Cholesterol,FBS_over_120,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope_of_depression,Number_of_vessels_fluro,Thallium]])[0][0] * 100
    pred1 = classificador.predict_proba([[Age,Sex,Chest_pain_type,BP,Cholesterol,FBS_over_120,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope_of_depression,Number_of_vessels_fluro,Thallium]])[0][1] * 100

    if predicao == 0:
        pred = 'Absence'
    else:
       
        pred = 'Presence'
    
    return pred, int(pred0), int(pred1)

def main():

    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Predição Doença Cardíaca</h1> 
    </div> 
    """

    st.markdown(html_temp, unsafe_allow_html= True)

    Age = st.number_input("Age", min_value=0, max_value= 150, value= 0, step=1)
    Sex = st.selectbox("Sex", ("Male", "Female"))
    Chest_pain_type = st.number_input("Chest pain type",min_value=1, max_value=4, step=1, value=1)
    BP = st.number_input("BP", min_value=0, step=1, value=1)
    Cholesterol = st.number_input("Cholesterol", min_value=0, step=1, value=1)
    FBS_over_120 = st.number_input("FBS over 120", min_value=0, max_value=1,step=1,value=0)
    EKG_results = st.number_input("EKG results", min_value=0, max_value=2, step=1, value=0)
    Max_HR = st.number_input("Max HR", min_value=0, step=1, value=1)
    Exercise_angina = st.number_input("Exercise angina", min_value=0, max_value=1, step=1)
    ST_depression = st.number_input("ST depression", min_value=0.0, step=0.1)
    Slope_of_ST = st.number_input("Slope of ST", min_value=1, max_value=3,step=1)
    Number_of_vessels_fluro = st.number_input("Number of vessels fluro", min_value=0, max_value=3, step=1)
    Thallium = st.selectbox("Thallium", (3,7,6))
    result = ""

    if st.button("Predict"):
        result, result0, result1 = predicao(Age,Sex,Chest_pain_type,BP,Cholesterol,FBS_over_120,EKG_results,Max_HR,Exercise_angina,ST_depression,Slope_of_ST,Number_of_vessels_fluro,Thallium)
        if result == "Absence":
            st.success("%s , Com probabilidade de %.2f%%" % (result, result0))
        else:
            st.success("%s , Com probabilidade de %.2f%%" % (result, result1))


if __name__=='__main__': 
    main()
