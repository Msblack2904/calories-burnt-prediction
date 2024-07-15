import numpy as np
import pickle
import streamlit as st
import xgboost 



model = pickle.load(open('model.pkl','rb'))

def predict_price(gender,age,height,weight,duration,heart_rate,body_temp):
    x = np.zeros(7)
    
    x[0] = np.array([[gender]]).astype(np.int64)
    x[1]= np.array([[age]]).astype(np.int64)
    x[2]= np.array([[height]]).astype(np.float64)
    x[3]= np.array([[weight]]).astype(np.float64)
    x[4]= np.array([[duration]]).astype(np.float64)
    x[5]= np.array([[heart_rate]]).astype(np.float64)
    x[6]= np.array([[body_temp]]).astype(np.float64)
    prediction =model.predict([x])[0]
    return float(prediction)

def main():
    html_temp = """ 
    <div style ="background-color:brown;padding:10px"> 
    <h1 style ="color:black;text-align:center;">Calories Burnt Predictor </h1>
    </div><br><br> 
    """
    st.markdown(html_temp, unsafe_allow_html = True) 

    Gender = st.selectbox('Select your gender', ['Male','Female'])
    if Gender == 'Male':
        gender = 1
    else:
        gender = 0
    age = st.text_input('Enter you age:')
    height = st.text_input('Enter you height (in cm):')
    weight = st.text_input('Enter you weight (in kg):')
    duration = st.text_input('Enter duration of your workout (in min):')
    heart_rate = st.text_input('Enter your current heart rate (beats per minute):')
    body_temp = st.text_input('Enter your current body temperatue (in degree celsius):')
    if st.button("predict the calories burnt"):
        output = round(predict_price(gender,age,height,weight,duration,heart_rate,body_temp),2)
        st.success(f"The calories burnt: {output}Kcal")

if __name__=='__main__':
    main()
