import streamlit as st

import sender
import pandas as pd
import json
import matplotlib.pyplot as plt


def get_values():
    y = sender.get_drift()
    data = json.loads(y)
    data = pd.DataFrame(data).drop(columns=["Unnamed: 0"])
    data["auc"] = data["auc"].astype('float')
    
    return data

data = get_values()

fig, ax = plt.subplots()
print(data.auc)
ax.plot(data.auc)

st.pyplot(fig)