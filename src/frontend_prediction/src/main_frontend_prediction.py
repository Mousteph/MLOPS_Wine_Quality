import streamlit as st
from sender import get_prediction

st.set_page_config(
    page_title="Red Wine",
    page_icon="🍷",
    layout="wide"
)

path_image = "https://i.pinimg.com/originals/55/52/9c/55529c372a893066ccad6faeda5292b4.jpg"
path_image = "wallpaper.jpg"

st.image(path_image, use_column_width=True, caption="Alcohol abuse is dangerous for health")

st.title("Red Wine Quality")

st1, st2 = st.columns(2)

fixed_aci = st1.number_input("Fixed acidity", min_value=4.60, max_value=15.60, value=8.30)
vol_aci = st2.number_input("Volatile acidity", min_value=0.12, max_value=1.58, value=0.53)

citric_acid = st1.number_input("Citric acid", min_value=0.00, max_value=0.79, value=0.26)
sulfur_dioxide = st2.number_input("Sulfur dioxide", min_value=6.00,
                                  max_value=165.00, value=44.96)

ph = st1.number_input("pH", min_value=2.86, max_value=4.01, value=3.32)
alcohol = st2.number_input("Alcohol", min_value=8.40, max_value=14.00, value=10.45)


def format_price(price: float) -> str:
    return f"{int(price):_} $".replace('_', ' ')

def format_prediction():
    return {
        "data": [fixed_aci, vol_aci, citric_acid, sulfur_dioxide, ph, alcohol]
    }
    
def format_quality(quality: float):
    if quality < 0.5:
        data = f"Pretty bad wine 🫗"
    else:
        data = f"Good wine 🍷"
        
    return data

st.write("#")

if st.button("Predict"):
    data = format_quality(0.2)
else:
    data = format_quality(1)
    
st.write(f"""
              ## {data}""")

# y = get_prediction({
#        "data": [size, nb_rooms, garden == "Yes"]
#        })
#
#    if not y["status"]:
#        st.error(f"Error during prediction: " + y["message"])
#    else:
#        st.write(f"Predicted price {format_price(y['data'])}")
