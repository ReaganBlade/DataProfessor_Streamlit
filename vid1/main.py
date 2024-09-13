import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
    Simple stock price app
Shown are the stock closing prices
""")

tickerSymbol = 'GOOGL'

# Get Data Using Ticker
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write(tickerDf)

# st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


st.write("High Chart")
st.line_chart(tickerDf.High)
st.write("Low Chart")
st.line_chart(tickerDf.Low)