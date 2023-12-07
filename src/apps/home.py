import pandas as pd 
import numpy as np 
import datetime
import pickle 
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

# streamlit run src\apps\home.py 


st.header("Flood Guard - Bangladesh Central Regions (Dhaka, Khulna, Mymensingh, and Narayanganj)")

st.write("""
Bangladesh is a country in South Asia that is known for its rich natural beauty and biodiversity. 
It has the world's largest delta, formed by the confluence of the Ganges, Brahmaputra and Meghna rivers, which supports a variety of ecosystems and wildlife. 
Bangladesh also faces the challenge of frequent floods, which affect millions of people every year and cause damage to crops, infrastructure and livelihoods.
The project aims to predict precipitation and prevent or reduce damage.
""")

st.write("""
Problem Statement:
The aftermath of flooding in Bangladesh results in immediate and long-term challenges, including loss of lives, destruction of crops, damage to infrastructure, and displacement of communities. 
        Timely and accurate flood prediction and waterbody forecasting are crucial for reducing the impact of floods, enabling better disaster preparedness, and facilitating effective resource allocation.
""")

# Load the datasets
forecast = pd.read_csv('predicted_precipitation.csv')
forecast['datetime'] = pd.to_datetime(forecast['datetime']).dt.date
actual = pd.read_csv("validation.csv")

default_date = datetime.date(2023, 8, 17)
date = st.date_input("Please select a date between 2022 Jan 1 and 2023 Aug 17 to see the precipitation forecast:", default_date)

# Check if the date is within the DataFrame's date range
if date in forecast['datetime'].values:
    selected_row = forecast[forecast['datetime'] == date]
    st.write(selected_row)
else:
    st.write("No data available for the selected date.")

actual = go.Scatter(
                    x = forecast['datetime'],
                    y = actual['precip'],
                    mode = 'lines',
                    name = 'Actual'
)

forecast = go.Scatter(x = forecast['datetime'],
                      y = forecast['predicted_precip'],
                      mode = 'lines',    
                      name = 'Forecast',
                      line=dict(color='#cc0000')
)

data = [actual, forecast]

# Create a layout
layout = go.Layout(
    title = 'Actual VS. Forecast between 2022 Jan 1 and 2023 Aug 17',
    xaxis = dict(title = 'Date'),
    yaxis = dict(title = 'Precipitation'),
)

# Create a figure
fig = go.Figure(data=data, layout=layout)

# Display the figure
st.plotly_chart(fig)


# tMain function to display the web app UI  
def main(): 


     
    if __name__=='__main__': 
        main() 