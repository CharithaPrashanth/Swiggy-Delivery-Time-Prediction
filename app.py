# importing the libraries
import streamlit as st
import pandas as pd
import pickle
from xgboost import XGBRegressor
from datetime import date

import base64


with open("Rainy Night Delivery Rider in City Lights.png", "rb") as f:
    encoded_image = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <style>

    /* Background image */
    .stApp {{
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.35),
                rgba(0, 0, 0, 0.35)
            ),
            url("data:image/png;base64,{encoded_image}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Input labels */
    label {{
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 17px !important;
        text-shadow: 1px 1px 3px #000000;
        background-color: rgba(0, 0, 0, 0.35);
        padding: 3px 8px;
        border-radius: 5px;
    }}

    /* Black prediction card */
    .st-key-prediction_card {{
        background-color: #000000 !important;
        padding: 30px 20px;
        border-radius: 10px;
        border: 1px solid #333333;
    }}

    /* Prediction heading */
    .prediction-title {{
        color: #ffffff !important;
        font-size: 30px !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 25px;
    }}

    /* Prediction value */
    .prediction-number {{
        color: #b54a00 !important;
        font-size: 64px !important;
        font-weight: 800 !important;
        text-align: center;
        line-height: 1.2;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# importing the model
with open ('swiggydeliverytime.pkl','rb') as f:
    model = pickle.load(f)

# importing the dataframe
df = pd.read_csv(r'swiggy_demographic.csv')

st.title('Swiggy Delivery Time Prediction')

col1,col2,col3 = st.columns(3)

with col1:
   ratings = st.selectbox('Driver Ratings',[1,2,3,4,5])
with col2:
    age = st.number_input('Driver Age',min_value = 20,max_value=50,step=1)
with col3:
 Pickup_Time = st.selectbox('Food prep time',['Short','Medium','Long'])
 if Pickup_Time == 'Short':
    pickup_time_minutes = 5
 elif Pickup_Time == 'Medium':
    pickup_time_minutes = 10
 else:
    pickup_time_minutes = 15

col4,col5,col6 = st.columns(3)
with col4:
   Distance = st.number_input('Distance (Km)',min_value=0,max_value=25)
with col5:
   Multiple_Deliveries = st.selectbox('Number of deliveries',[0,1,2,3])
with col6:
   order_time = st.selectbox('Ordered Time',range(0,24))

col7,col8,col9 = st.columns(3)
with col7:
   weekend = st.selectbox('Weekend',['Yes','No'])
   if weekend == 'Yes':
        week = 1
   else:
       week = 0
with col8:
   traffic= st.selectbox('Traffic',['high', 'jam', 'low', 'medium',])
with col9:
   Vehicle_type = st.selectbox('Vehicle',['motorcycle', 'scooter', 'electric_scooter', 'bicycle'])

col10,col11,col12 = st.columns(3)
with col10:
   weather = st.selectbox('Weather',['sunny', 'stormy', 'sandstorms', 'cloudy', 'fog', 'windy'])
with col11:
   order_type = st.selectbox('Order Type',['snack', 'drinks', 'buffet', 'meal'])
with col12:
   festival = st.selectbox('Festival',['Yes','No'])

col13,col14,col15 = st.columns(3)
with col13:
   city = st.selectbox('City',[  'INDO',   'BANG',  'COIMB',   'CHEN',    'HYD', 'RANCHI',    'MYS',
    'DEH',    'KOC',   'PUNE',   'LUDH',    'KNP',    'MUM',    'KOL',
    'JAP',    'SUR',    'GOA',   'AURG',    'AGR',    'VAD',    'ALH',
    'BHP'])
with col14:
   day = st.selectbox('Day',[ 'monday','tuesday', 'wednesday', 'thursday','friday','saturday','sunday'])
with col15:
    time_of_day = st.selectbox('Time of the day',['morning', 'evening', 'afternoon', 'night', 'after_midnight'])

col16,col17,col18 = st.columns(3)
with col16:
   city_type = st.selectbox('City Type',['urban', 'metropolitian', 'semi-urban'])
with col17:
   vehicle_condition = st.selectbox('Vehicle Condition',['Poor','Average','Good','Excellent'])
   if vehicle_condition == 'Poor':
        condition = 0
   elif vehicle_condition == 'Average':
        condition = 1
   elif vehicle_condition == 'Good':
           condition = 2
   else:
        condition = 3
with col18:
   order_month = st.selectbox('Order Month',range(1,13))

today = date.today()

is_even = 1 if today.day % 2 == 0 else 0



if st.button('Predict'):

    input_df = pd.DataFrame({
        'age': [age],
        'ratings': [ratings],
        'weather': [weather],
        'traffic': [traffic],
        'vehicle_condition': [condition],
        'type_of_order': [order_type],
        'type_of_vehicle': [Vehicle_type],
        'multiple_deliveries': [Multiple_Deliveries],
        'festival': [festival],
        'city_type': [city_type],
        'city_name': [city],
        'order_month': [order_month],
        'order_day_of_week': [day],
        'is_weekend': [week],
        'pickup_time_minutes': [pickup_time_minutes],
        'order_time_hour': [order_time],
        'order_time_of_day': [time_of_day],
        'distance': [Distance],
        'is_even_day': [is_even]
    })

    # Generate prediction
    prediction = model.predict(input_df)[0]

    # Display the prediction card
    with st.container(key="prediction_card"):

        st.markdown(
            '<div class="prediction-title">'
            'Estimated Delivery Time'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="prediction-number">'
            f'{prediction:.2f} Mins'
            '</div>',
            unsafe_allow_html=True
        )
