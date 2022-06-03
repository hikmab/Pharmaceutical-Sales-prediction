import streamlit as st
import awesome_streamlit as ast



def write():
    """Used to write the page in the app.py file"""
    st.title('LSTM Forecasting')
    st.write('Rossman Pharmaceuticals as a Machine Learning Engineer. The finance team wants to forecast sales in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgment to forecast sales.')
    st.write('The data team identified factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.')
    
    st.write('---')
    st.markdown('## Descriptive Statistics and Visualization of the data')
    st.image("./image/mm9.png")
    
    st.write('---')
    st.markdown('## Removing Stationarity')
    st.image("./image/mm10.png")
    
    st.write('---')
    st.markdown('## Define and Estimate the LSTM')
    st.image("./image/mm11.png")


    st.write('---')
    st.markdown('## Forecast the LSTM on the Validation Set and Assess Accuracy')
    st.image("./image/mm12.png")
   