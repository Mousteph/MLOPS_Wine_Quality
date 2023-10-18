import streamlit as st

import sender
import pandas as pd
import json
from typing import Tuple

st.set_page_config(
    page_title="Red Wine Data Drift",
    page_icon="🍸",
    layout="wide"
)

path_image = "wallpaper.jpg"

st.image(path_image, use_column_width=True, caption="Alcohol abuse is dangerous for health")

st.title("Red Wine Data Drift")

last_AUC = None
date = None
chart_data = None

def get_drift(new:bool = False) -> pd.DataFrame:
    """Get data drift from backend

    Args:
        new (bool, optional): If True, get new data drift. Defaults to False.

    Returns:
        pd.DataFrame: DataFrame of data drift
    """
    
    if new:
        y = sender.new_drift()
    else:
        y = sender.refresh_drift()
        
    if not y["status"]:
        st.error(f"Error during checking data drift: {y['message']}")
        return None
    else:
        d = json.loads(y["data"])
        return pd.DataFrame(d).drop(columns=["Unnamed: 0"])
    
def update_auc(data: pd.DataFrame) -> Tuple:
    """Update AUC and date from data drift

    Args:
        data (pd.DataFrame): DataFrame of data drift

    Returns:
        Tuple: Tuple of (date, AUC)
    """
    
    if data is not None and len(data) != 0:
        last = data.iloc[-1]
        return last.iloc[0], last.iloc[1]
    
    return None, None

data = get_drift()
date, last_AUC = update_auc(data)
chart_data = data

st.write(f"""
         ###
         ## Last AUC ({date}): {last_AUC}
         ###
         """)

if st.button("Refresh"):
    data = get_drift()
    date, last_AUC = update_auc(data)
    chart_data = data
    
period = st.number_input("Number of periods", min_value=-1, value=20)

st.write("###")

if chart_data is not None:
    if period != -1:
        chart_data = chart_data.iloc[-period:]
    
    st.line_chart(chart_data, x="Date", y="AUC")

st.write("##")

if st.button("Test New Entries"):
    data = get_drift(True)
    date, last_AUC = update_auc(data)
    chart_data = data
