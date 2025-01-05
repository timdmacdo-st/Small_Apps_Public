import streamlit as st
import numpy as np

available_hours_array = np.array([0, 1, 2, 4, 8, 16])
available_hours_scale = np.array([4, 2, 1.5, 1, 0.75, 0.5])

def scale_factor(hours_available):
    scale = np.interp(hours_available, available_hours_array, available_hours_scale)
    return scale

def get_base_time_value():
    base_value = 1.20 * 60
    return base_value

def calculate(time_hr, cost, hours_available):
    scale = scale_factor(hours_available)
    value_per_hr = get_base_time_value()
    scaled_value_for_time = value_per_hr * scale * time_hr

    if scaled_value_for_time > cost:
        return f"Better to <span style='color: blue;'>spend money</span>, estimated value is ${scaled_value_for_time:.2f}", "spend money"
    else:
        return f"Better to <span style='color: orange;'>spend time</span>, estimated value is ${scaled_value_for_time:.2f}", "spend time"

# Streamlit UI
st.title("Time vs Cost Decision Helper")

st.sidebar.header("Input Parameters")

# Time input options
input_type = st.sidebar.radio("Input time in:", ("Minutes", "Hours"))

if input_type == "Minutes":
    time_min = st.sidebar.number_input("Time required (minutes):", min_value=0.0, step=5.0, value=60.0)
    time_hr = time_min / 60
else:
    time_hr = st.sidebar.number_input("Time required (hours):", min_value=0.0, step=0.5, value=1.0)

cost = st.sidebar.number_input("Cost to outsource ($):", min_value=0.0, step=10.0, value=60.0)
hours_available = st.sidebar.slider("Hours available today:", min_value=0, max_value=16, value=4, step=1)

# Calculation
if st.sidebar.button("Calculate"):
    result, decision = calculate(time_hr, cost, hours_available)
    st.markdown(f"<h2>{result}</h2>", unsafe_allow_html=True)
