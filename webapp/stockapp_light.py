import streamlit as st

import yfinance as yf

import plotly.graph_objects as go

st.set_page_config(
    page_title="YFinance",
    page_icon="📈",
)

st.markdown(
    """
    # Stock situation (YFinance)
    This is my demo of YFinance with Streamlilt
    """
)

data = yf.download(tickers="AI.PA", period='1mo', interval='1d', multi_level_index=False)
data = data[data["High"] != data["Low"]]

fig = go.Figure(data=[go.Candlestick(x=data.index,
                                    open=data["Open"],
                                    high=data["High"],
                                    low=data["Low"],
                                    close=data['Close']
                                    )]
                )
tab_chart, tab_data = st.tabs(["Chart", "Data"])

st.plotly_chart(fig, use_container_width=True)

st.dataframe(data)
