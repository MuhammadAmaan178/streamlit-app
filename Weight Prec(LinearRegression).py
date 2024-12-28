import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


m_data ={
    'Height (cm)': [170,175,180,185,190,165,178,188,172,185],
    'Age (years)': [25,30,35,40,45,28,32,38,27,40],
    'Weight (kg)': [72,80,85,90,95,70,82,88,75,90]
}

f_data ={
    'Height (cm)': [160,165,170,155,168,160,172,158,162,170],
    'Age (years)': [25,30,35,40,45,28,32,38,27,40],
    'Weight (kg)': [58,63,68,52,65,60,65,55,62,66]
}


def m_prec(height, age):
    df = pd.DataFrame(m_data)

    X = df[['Height (cm)', 'Age (years)']]
    Y = df[['Weight (kg)']]
    reg = LinearRegression()
    reg.fit(X, Y)
    prec = reg.predict([[height, age]])
    st.subheader("Prediction Weight:-")
    st.text(f"On Basis Of Your Height, Age and Gender...Your Weight Can Be Around {prec}")
    st.warning("Note:- Your Weight Also Depends On Other Factors Like Body Composition, Diet and Nutrition, Physical Activity and so on... This Predicted Value Can Be Full Of Errors!!!")

    st.subheader("Linear Regression Plot")
    st.text("For Height and Weight")
    fig, ax = plt.subplots()
    plt.scatter(df['Height (cm)'], df['Weight (kg)'], color='blue', marker='+')
    plt.scatter(height, prec, color='red')
    plt.axhline(y=prec, color='red')
    plt.axvline(x=height, color='red')
    plt.title('Height vs. Weight')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    st.pyplot(fig)

    st.text("For Age and Weight")
    fig, ax = plt.subplots()
    plt.scatter(df['Age (years)'], df['Weight (kg)'], color='green', marker='+')
    plt.title('Age vs. Weight')
    plt.xlabel('Age (years)')
    plt.ylabel('Weight (kg)')
    plt.scatter(age, prec, color='red')
    plt.axhline(y=prec, color='red')
    plt.axvline(x=age, color='red')
    st.pyplot(fig)


def f_prec(height, age):
    df = pd.DataFrame(f_data)

    X = df[['Height (cm)', 'Age (years)']]
    Y = df[['Weight (kg)']]
    reg = LinearRegression()
    reg.fit(X, Y)
    prec = reg.predict([[height, age]])
    st.subheader("Prediction Weight:-")
    st.text(f"On Basis Of Your Height, Age and Gender...Your Weight Can Be Around {prec}")
    st.warning(
        "Note:- Your Weight Also Depends On Other Factors Like Body Composition, Diet and Nutrition, Physical Activity and so on... This Predicted Value Can Be Full Of Errors!!!")

    st.subheader("Linear Regression Plot")
    st.text("For Height and Weight")
    fig, ax = plt.subplots()
    plt.scatter(df['Height (cm)'], df['Weight (kg)'], color='blue', marker='+')
    plt.scatter(height, prec, color='red')
    plt.axhline(y=prec, color='red')
    plt.axvline(x=height, color='red')
    plt.title('Height vs. Weight')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    st.pyplot(fig)

    st.text("For Age and Weight")
    fig, ax = plt.subplots()
    plt.scatter(df['Age (years)'], df['Weight (kg)'], color='green', marker='+')
    plt.title('Age vs. Weight')
    plt.xlabel('Age (years)')
    plt.ylabel('Weight (kg)')
    plt.scatter(age, prec, color='red')
    plt.axhline(y=prec, color='red')
    plt.axvline(x=age, color='red')
    st.pyplot(fig)


st.title('Predict Your Weight')
height = st.number_input("Enter Your Height(in cm)",min_value=45,max_value=272,help="Height Should Be In 'cm'")
age = st.number_input("Enter Your Age(in years)",min_value=0,max_value=164,help="Age Should Be In 'years'")
gender = st.selectbox(label="Select your gender",options=["Male" , "Female"])

if st.button("Done!!!"):
    if gender == "Male":
        m_prec(height, age)
    elif gender == "Female":
        f_prec(height, age)


