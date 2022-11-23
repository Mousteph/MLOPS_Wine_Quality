import streamlit as st
from sender import get_prediction

size = st.number_input("House size", min_value=0.0, value=0.0)
nb_rooms = st.number_input("Number of rooms", min_value=1, value=1)
garden = st.selectbox("Garden?", ["Yes", "No"])

def format_price(price: float) -> str:
    return f"{int(price):_} $".replace('_', ' ')

def prediction():
    X = np.array([[size, nb_rooms, garden == "Yes"]])
    return model.predict(X)[0]

if st.button("Predict"):
    y = get_prediction({
        "data": [size, nb_rooms, garden == "Yes"]
        })

    if not y["status"]:
        st.error(f"Error during prediction: " + y["message"])
    else:
        st.write(f"Predicted price {format_price(y['data'])}")
