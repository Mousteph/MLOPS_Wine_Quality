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

path_image = "wallpaper.jpg"

st.image(path_image, use_column_width=True, caption="Alcohol abuse is dangerous for health")

st.title("Red Wine Data Drift")

last_AUC = 0.5
date = ""

st.write(f"""
         ###
         ## Last AUC ({date}): {last_AUC}
         ###
         """)

if st.button("Refresh"):
    pass

st.write("###")

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['AUC', "Date"]
)

st.line_chart(chart_data, x="Date", y="AUC")

st.write("##")

if st.button("Test New Entries"):
    pass




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