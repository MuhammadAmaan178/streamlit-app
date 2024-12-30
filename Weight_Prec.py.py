import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from backend import *

st.title('Predict Your Weight')
height = st.number_input("Enter Your Height(in cm)",min_value=45,max_value=272,help="Height Should Be In 'cm'")
age = st.number_input("Enter Your Age(in years)",min_value=10,max_value=164,help="Age Should Be In 'years'")
gender = st.selectbox(label="Select your gender",options=["Male" , "Female"])
physique = st.selectbox(label="Select your physique",options=["Thin" , "Average", "Fat"])

if st.button("Done!!!"):
    if gender == "Male":
        if physique == "Thin":
            prec = m_th_prec(height, age)
            df = m_th_dataframe()
        elif  physique == "Average":
            prec = m_avg_prec(height, age)
            df = m_avg_dataframe()
        elif  physique == "Fat":
            prec = m_fat_prec(height, age)
            df = m_fat_dataframe()
    elif gender == "Female":
        if physique == "Thin":
            prec = f_th_prec(height, age)
            df = f_th_dataframe()
        elif physique == "Average":
            prec = f_avg_prec(height, age)
            df = f_avg_dataframe()
        elif physique == "Fat":
            prec = f_fat_prec(height, age)
            df = f_fat_dataframe()


    st.subheader("Prediction Weight:-")
    st.text(f"On Basis Of Your Height, Age and Gender...Your Weight Can Be Around {prec}")
    st.warning("Note:- Your Weight Also Depends On Other Factors Like Body Composition, Diet and Nutrition, Physical Activity and so on... This Predicted Value Can Be Full Of Errors!!!")


    st.subheader("Linear Regression Plot")
    st.text("For Height and Weight")
    fig, ax = plt.subplots()
    plt.scatter(df['Height'], df['Weight'], color='blue', marker='+')
    plt.scatter(height, prec, color='red')
    plt.axhline(y=prec, color='red')
    plt.axvline(x=height, color='red')
    plt.title('Height vs. Weight')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    st.pyplot(fig)


    st.text("For Age and Weight")
    fig, ax = plt.subplots()
    plt.scatter(df['Age'], df['Weight'], color='green', marker='+')
    plt.title('Age vs Weight')
    plt.xlabel('Age (years)')
    plt.ylabel('Weight (kg)')
    plt.scatter(age, prec, color='red')
    plt.axhline(y=prec, color='red')
    plt.axvline(x=age, color='red')
    st.pyplot(fig)

