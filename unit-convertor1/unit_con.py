import streamlit as st
import requests

# Dark and light theme
theme = st.sidebar.radio("Select Theme 🎨", ["Light ☀️", "Dark 🌙"])

# Custom CSS based on theme
if theme == "Dark 🌙":
    st.markdown(
        """
        <style>
        body, .stApp {
            background: linear-gradient(135deg, #1e1e2f, #2d2d44);
            color: white;
        }
        h1 {
            color: white;
        }
        .stButton>button {
            background: linear-gradient(45deg, #0b5394, #351c75);
            color: white;
            box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #92fe9d, #00c9ff);
            color: black;
        }
        .result-box {
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
        }
        .stNumberInput>div>input, .stSelectbox>div>div>select {
            background: rgba(255, 255, 255, 0.1);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .footer {
            color: rgba(255, 255, 255, 0.7);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:  # Light theme
    st.markdown(
        """
        <style>
        body, .stApp {
            background: linear-gradient(135deg, #e0f7fa, #b2ebf2);
            color: #333;
        }
        h1 {
            color: #333;
        }
        .stButton>button {
            background: linear-gradient(45deg, #42a5f5, #29b6f6);
            color: white;
            box-shadow: 0px 5px 15px rgba(66, 165, 245, 0.4);
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #aed581, #81c784);
            color: black;
        }
        .result-box {
            background: rgba(255, 255, 255, 0.8);
            box-shadow: 0px 5px 15px rgba(100, 181, 246, 0.3);
        }
        .stNumberInput>div>input, .stSelectbox>div>div>select {
            background: rgba(255, 255, 255, 0.8);
            color: #333;
            border: 1px solid rgba(100,100,100,0.3);
        }
        .footer {
            color: rgba(0, 0, 0, 0.7);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Title and description
st.markdown("<h1>Unit Converter 📏 ⚖️ 🌡️</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, temperature, and more!")

# Sidebar menu
conversion_type = st.sidebar.selectbox(
    "Select Conversion Type 🔄",
    ["Length 📏", "Weight ⚖️", "Temperature 🌡️", "Volume 🧴", "Area 📐", "Speed 🚀", "Time ⏰", "Energy ⚡", "Currency 💱"],
)
value = st.number_input("Enter Value 🔢", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Unit selection based on conversion type
if conversion_type == "Length 📏":
    with col1:
        from_unit = st.selectbox(
            "From ➡️", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
        )
    with col2:
        to_unit = st.selectbox(
            "To ⬅️", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
        )
elif conversion_type == "Weight ⚖️":
    with col1:
        from_unit = st.selectbox(
            "From ➡️", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"]
        )
    with col2:
        to_unit = st.selectbox(
            "To ⬅️", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"]
        )
elif conversion_type == "Temperature 🌡️":
    with col1:
        from_unit = st.selectbox("From ➡️", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To ⬅️", ["Celsius", "Fahrenheit", "Kelvin"])
elif conversion_type == "Volume 🧴":
    with col1:
        from_unit = st.selectbox("From ➡️", ["Liters", "Milliliters", "Gallons", "Cubic Meters"])
    with col2:
        to_unit = st.selectbox("To ⬅️", ["Liters", "Milliliters", "Gallons", "Cubic Meters"])
elif conversion_type == "Area 📐":
    with col1:
        from_unit = st.selectbox("From ➡️", ["Square Meters", "Square Feet", "Square Kilometers", "Hectares"])
    with col2:
        to_unit = st.selectbox("To ⬅️", ["Square Meters", "Square Feet", "Square Kilometers", "Hectares"])
elif conversion_type == "Speed 🚀":
    with col1:
        from_unit = st.selectbox("From ➡️", ["Meters/Second", "Kilometers/Hour", "Miles/Hour", "Feet/Second"])
    with col2:
        to_unit = st.selectbox("To ⬅️", ["Meters/Second", "Kilometers/Hour", "Miles/Hour", "Feet/Second"])
elif conversion_type == "Time ⏰":
    with col1:
        from_unit = st.selectbox("From ➡️", ["Seconds", "Minutes", "Hours", "Days"])
    with col2:
        to_unit = st.selectbox("To ⬅️", ["Seconds", "Minutes", "Hours", "Days"])
elif conversion_type == "Energy ⚡":
    with col1:
        from_unit = st.selectbox("From ➡️", ["Joules", "Calories", "Kilowatt-hours"])
    with col2:
        to_unit = st.selectbox("To ⬅️", ["Joules", "Calories", "Kilowatt-hours"])
elif conversion_type == "Currency 💱":
    with col1:
        from_unit = st.selectbox("From ➡️", ["USD", "EUR", "GBP", "JPY", "INR"])
    with col2:
        to_unit = st.selectbox("To ⬅️", ["USD", "EUR", "GBP", "JPY", "INR"])

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9 / 5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5 / 9
        elif to_unit == "Kelvin":
            return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9 / 5 + 32
    return value

def volume_converter(value, from_unit, to_unit):
    volume_units = {
        "Liters": 1,
        "Milliliters": 1000,
        "Gallons": 0.264172,
        "Cubic Meters": 0.001,
    }
    return value * (volume_units[to_unit] / volume_units[from_unit])

def area_converter(value, from_unit, to_unit):
    area_units = {
        "Square Meters": 1,
        "Square Feet": 10.7639,
        "Square Kilometers": 0.000001,
        "Hectares": 0.0001,
    }
    return value * (area_units[to_unit] / area_units[from_unit])

def speed_converter(value, from_unit, to_unit):
    speed_units = {
        "Meters/Second": 1,
        "Kilometers/Hour": 3.6,
        "Miles/Hour": 2.23694,
        "Feet/Second": 3.28084,
    }
    return value * (speed_units[to_unit] / speed_units[from_unit])

def time_converter(value, from_unit, to_unit):
    time_units = {
        "Seconds": 1,
        "Minutes": 1 / 60,
        "Hours": 1 / 3600,
        "Days": 1 / 86400,
    }
    return value * (time_units[to_unit] / time_units[from_unit])

def energy_converter(value, from_unit, to_unit):
    energy_units = {
        "Joules": 1,
        "Calories": 0.239006,
        "Kilowatt-hours": 0.000000277778,
    }
    return value * (energy_units[to_unit] / energy_units[from_unit])

def currency_converter(value, from_unit, to_unit):
    API_KEY = "YOUR_API_KEY"  # Replace with your API key
    url = f"https://api.exchangerate-api.com/v4/latest/{from_unit}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][to_unit]
    return value * rate

# Convert button
if st.button("🔄 Convert"):
    try:
        if conversion_type == "Length 📏":
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type == "Weight ⚖️":
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type == "Temperature 🌡️":
            result = temp_converter(value, from_unit, to_unit)
        elif conversion_type == "Volume 🧴":
            result = volume_converter(value, from_unit, to_unit)
        elif conversion_type == "Area 📐":
            result = area_converter(value, from_unit, to_unit)
        elif conversion_type == "Speed 🚀":
            result = speed_converter(value, from_unit, to_unit)
        elif conversion_type == "Time ⏰":
            result = time_converter(value, from_unit, to_unit)
        elif conversion_type == "Energy ⚡":
            result = energy_converter(value, from_unit, to_unit)
        elif conversion_type == "Currency 💱":
            result = currency_converter(value, from_unit, to_unit)
        st.markdown(
            f'<div class="result-box">{value} {from_unit} = {result:.4f} {to_unit}</div>',
            unsafe_allow_html=True,
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown(
    '<div class="footer">Created by Tayyeba Ali 👩‍💻</div>',
    unsafe_allow_html=True,
)