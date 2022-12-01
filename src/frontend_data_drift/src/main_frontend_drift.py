import streamlit as st

import sender
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Red Wine Data Drift",
    page_icon="🍸",
    layout="wide"
)

path_image = "../images/wallpaper.jpg"

st.image(path_image, use_column_width=True, caption="Alcohol abuse is dangerous for health")

st.title("Red Wine Data Drift")

last_AUC = None
date = None

def get_drift():
    y = sender.refresh_drift()
    if not y["status"]:
        st.error(f"Error during checking data drift: {y['message']}")
        return None
    else:
        d = json.loads(y["data"])
        print(y["data"])
        return pd.DataFrame(d).drop(columns=["Unnamed: 0"])
    
def update_auc(data):
    if data is not None and len(data) != 0:
        last = data.iloc[-1]
        return last[0], last[1]
    
    return None, None

data = get_drift()
date, last_AUC = update_auc(data)

st.write(f"""
         ###
         ## Last AUC ({date}): {last_AUC}
         ###
         """)

if st.button("Refresh"):
    data = get_drift()
    date, last_AUC = update_auc(data)

st.write("###")

# chart_data = pd.DataFrame(
#     np.random.randn(20, 2),
#     columns=['AUC', "Date"]
# )

# st.line_chart(chart_data, x="Date", y="AUC")

# st.write("##")

# if st.button("Test New Entries"):
#     pass




# def get_values():
#     y = sender.get_drift()
#     data = json.loads(y)
#     data = pd.DataFrame(data).drop(columns=["Unnamed: 0"])
#     data["auc"] = data["auc"].astype('float')
    
#     return data

# data = get_values()

# fig, ax = plt.subplots()
# print(data.auc)
# ax.plot(data.auc)

# st.pyplot(fig)