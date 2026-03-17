import streamlit as st

import plotly.graph_objects as go

from yfin import data_loader


@st.cache_data
def cached_data_loader(ticker: str, period: str):
    return data_loader.extract_data(ticker, period)


st.set_page_config(
    page_title="YFinance",
    page_icon="📈",
)

with st.sidebar:
    st.header("Plotting Demo")

    values = data_loader.get_values()

    selected_value = st.selectbox("Choose a ticker", values.keys())

    selected_period = st.selectbox("Choose a period:",
                                   data_loader.PERIOD_VALUES,
                                   index=2
                                   )


st.markdown(
    """
    # Stock situation (YFinance)
    This is my demo of YFinance with Streamlilt
    """
)

data = cached_data_loader(values[selected_value], selected_period)

fig = go.Figure(data=[go.Candlestick(x=data.index,
                                    open=data["Open"],
                                    high=data["High"],
                                    low=data["Low"],
                                    close=data['Close']
                                    )]
                )
tab_chart, tab_data = st.tabs(["Chart", "Data"])

with tab_chart:
    st.plotly_chart(fig, use_container_width=True)

with tab_data:
    st.dataframe(data)
