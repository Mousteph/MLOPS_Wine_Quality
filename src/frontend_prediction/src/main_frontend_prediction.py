import streamlit as st
from sender import get_prediction
from typing import Dict

st.set_page_config(
    page_title="Red Wine",
    page_icon="🍷",
    layout="wide"
)

path_image = "wallpaper.jpg"

st.image(path_image, use_column_width=True, caption="Alcohol abuse is dangerous for health")

st.title("Red Wine Quality")

st1, st2 = st.columns(2)

fixed_aci = st1.number_input("Fixed acidity", min_value=4.60, value=8.30)
vol_aci = st2.number_input("Volatile acidity", min_value=0.12, value=0.53)

citric_acid = st1.number_input("Citric acid", min_value=0.00, value=0.26)
sulfur_dioxide = st2.number_input("Sulfur dioxide", min_value=6.00, value=44.96)

ph = st1.number_input("pH", min_value=2.86, value=3.32)
alcohol = st2.number_input("Alcohol", min_value=8.40, value=10.45)


def format_prediction() -> Dict[str, float]:
    """Return formatted prediction

    Returns:
        Dict[str, float]: Tuple of input data
    """
    
    return {
        "data": [fixed_aci, vol_aci, citric_acid, sulfur_dioxide, ph, alcohol]
    }
    
def format_quality(quality: float) -> str:
    """Format quality prediction

    Args:
        quality (float): Value of quality

    Returns:
        str: Message of quality of wine
    """
    
    if quality <= 0.5:
        data = "Pretty bad wine 🫗"
    else:
        data = "Good wine 🍷"
        
    return data

st.write("#")

if st.button("Predict"):
    y = get_prediction(format_prediction())
    if not y["status"]:
        st.error(f"Error during prediction: {y['message']}")
    else:
        data = format_quality(y['data'])
        st.write(f"""## {data}""")
 