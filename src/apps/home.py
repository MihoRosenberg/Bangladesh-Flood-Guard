import pandas as pd 
import numpy as np 
import datetime
import pickle 
import h5py
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

# streamlit run src\apps\home.py 

def display_header():
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

# load model
def load_model(model_file):
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
    return model 

def load_data(file, date_col):
     df = pd.read_csv(file, parse_dates=[date_col])
     return df

def get_data(df, date):
    data = df.loc[date]
    return data

def get_date_range(df, date_col):
    start_date = df[date_col].min()
    end_date = df[date_col].min()
    start_end_date = [start_date, end_date]
    return start_end_date


def get_prediction(model, data):
    pred = model.predict(data)
    return pred

def get_date(start_end_date, df, cols):
    default_date = datetime.date(2023, 8, 17)
    date = st.date_input("Please select a date between 2022 Jan 1 and 2023 Aug 17 to see the precipitation forecast:", default_date)
    if (date >= start_end_date[0]) & (date <= start_end_date[1]):
        weather_data = df.loc[date, cols]
        return weather_data
    else:
        st.write("No data available for the selected date.")

def display_forecast(date, predict):
    forecast_df = pd.DataFrame({'Date': date, 'Precipitation Forecast': predict})
    st.dataframe(forecast_df)

# Draw line charts
def plot_actual_forecast(forecast, actual, date_col, target_variable):
    actual = go.Scatter(x = forecast[date_col],
                        y = actual[target_variable],
                        mode = 'lines',
                        name = 'Actual')

    forecast = go.Scatter(x = forecast[date_col],
                          y = forecast[target_variable],
                          mode = 'lines',    
                          name = 'Forecast',
                          line=dict(color='#cc0000'))

    data = [actual, forecast]

    # Create a layout
    layout = go.Layout(title = 'Actual VS. Forecast between 2022 Jan 1 and 2023 Aug 17',
                       xaxis = dict(title = 'Date'),
                       yaxis = dict(title = 'Precipitation'))

    # Create a figure
    fig = go.Figure(data=data, layout=layout)

    # Display the figure
    st.plotly_chart(fig)

# Main function to display the web app UI  
def main(): 
    DATE_COLS = 'datetime'
    TARGET_VARIABLE = 'precip'
    # FEATURES_FOR_PREDICTION = 
    ACTUAL_DATASET = "validation.csv"
    FORECAST_DATASET = "predicted_precipitation.csv"
    
    # Display the header
    display_header()

    # Load the model
    model = load_model("..\artifactory\best_model.pkl")

    # Load datasets
    actual = load_data(ACTUAL_DATASET, DATE_COLS)
    forecast = load_data(FORECAST_DATASET, DATE_COLS)


    start_end_date = get_date_range(actual, DATE_COLS)

    # Get date
    date = get_date(start_end_date, actual)
        
    # Get the values for prediction
    data = get_data(actual, date)

    # Predict
    pred = get_prediction(model, data)

    # Display
    display_forecast(date, pred)
    
    # Draw line charts
    plot_actual_forecast(forecast, actual, DATE_COLS, TARGET_VARIABLE)
     
    if __name__=='__main__': 
        main() 