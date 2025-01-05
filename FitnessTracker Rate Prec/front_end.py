import streamlit as st
from back_end import *

st.markdown('<h1 style="text-align: center; font-size: 60px;">Fitness Tracker Rate</h1>', unsafe_allow_html=True)
st.image("fitness-tracker.webp", width=680)
brand = st.selectbox(label="Which Brand You Want?",options=['fire-boltt', 'boat', 'noise', 'honor', 'crossbeats', 'samsung',
       'garmin', 'huawei', 'dizo', 'gizmore', 'ambrane', 'zebronics',
       'pebble', 'hammer', 'apple', 'fitbit', 'amazfit', 'fossil'])
battery_life = st.number_input(label="Approx How Much Battery Life You Want?",min_value =1 ,max_value =22)

prec = predict(brand,battery_life)
st.subheader("Prediction Price:-")
st.text(f"To Buy A Fitness Tracker Of Above Brand with Above Battery Life You Sould AtLeast Have {prec}")
st.subheader("About Dataset:-")
st.warning("This is a fitness tracker product dataset consisting of different products from various brands with their specifications, ratings and reviews for the Indian market. The data has been collected from e-commerce websites namely Flipkart and Amazon using web scraping technique.")