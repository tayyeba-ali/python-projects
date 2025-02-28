import streamlit as st
import requests

#  page title and icon
st.set_page_config(page_title="📏  Unit Converter", page_icon="📏", layout="centered")

# Custom CSS 
st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: auto;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSelectbox, .stNumberInput {
        border-radius: 5px;
    }
    .stHeader {
        font-size: 2.5em;
        font-weight: bold;
        color: #4CAF50;
    }
    .stFooter {
        text-align: center;
        margin-top: 2em;
        color: #777;
    }
    .stSuccess {
        font-size: 1.2em;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="stHeader">📏 Ultimate Unit Converter</p>', unsafe_allow_html=True)
st.write("Convert between various units easily! Select a conversion type and enter the value.")

# Sidebar for theme selection
st.sidebar.header(" Settings")
theme = st.sidebar.selectbox("Choose a theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        .stHeader {
            color: #4CAF50;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
        }
        .stHeader {
            color: #4CAF50;
        }
        </style>
        """, unsafe_allow_html=True)

# Sidebar for conversion type selection
st.sidebar.header("🔧 Conversion Type")
conversion_type = st.sidebar.selectbox(
    "Choose a conversion type",
    ["Length", "Weight", "Temperature", "Volume", "Area", "Speed", "Currency", "Time", "Energy"]
)

# convert length
def convert_length(value, from_unit, to_unit):
    conversions = {
        "Meters": 1,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Centimeters": 100,
        "Yards": 1.09361
    }
    return value * (conversions[to_unit] / conversions[from_unit])

#  convert weight
def convert_weight(value, from_unit, to_unit):
    conversions = {
        "Kilograms": 1,
        "Pounds": 2.20462,
        "Ounces": 35.274,
        "Grams": 1000
    }
    return value * (conversions[to_unit] / conversions[from_unit])

# convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  

#  convert volume
def convert_volume(value, from_unit, to_unit):
    conversions = {
        "Liters": 1,
        "Milliliters": 1000,
        "Gallons": 0.264172,
        "Cubic Meters": 0.001
    }
    return value * (conversions[to_unit] / conversions[from_unit])

# convert area
def convert_area(value, from_unit, to_unit):
    conversions = {
        "Square Meters": 1,
        "Square Feet": 10.7639,
        "Square Kilometers": 0.000001,
        "Hectares": 0.0001
    }
    return value * (conversions[to_unit] / conversions[from_unit])

# convert speed
def convert_speed(value, from_unit, to_unit):
    conversions = {
        "Meters/Second": 1,
        "Kilometers/Hour": 3.6,
        "Miles/Hour": 2.23694,
        "Feet/Second": 3.28084
    }
    return value * (conversions[to_unit] / conversions[from_unit])

# convert currency
def convert_currency(value, from_unit, to_unit):
    API_KEY = "YOUR_API_KEY" 
    url = f"https://api.exchangerate-api.com/v4/latest/{from_unit}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][to_unit]
    return value * rate

# convert time
def convert_time(value, from_unit, to_unit):
    conversions = {
        "Seconds": 1,
        "Minutes": 1/60,
        "Hours": 1/3600,
        "Days": 1/86400
    }
    return value * (conversions[to_unit] / conversions[from_unit])

#  convert energy
def convert_energy(value, from_unit, to_unit):
    conversions = {
        "Joules": 1,
        "Calories": 0.239006,
        "Kilowatt-hours": 0.000000277778
    }
    return value * (conversions[to_unit] / conversions[from_unit])

# Main content based on conversion type
if conversion_type == "Length":
    st.header("📏 Length Conversion")
    length_units = ["Meters", "Feet", "Inches", "Centimeters", "Yards"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", length_units, key="length_from")
    with col2:
        to_unit = st.selectbox("To", length_units, key="length_to")
    value = st.number_input("Enter value", value=1.0, min_value=0.0, key="length_value")
    result = convert_length(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif conversion_type == "Weight":
    st.header("⚖️ Weight Conversion")
    weight_units = ["Kilograms", "Pounds", "Ounces", "Grams"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", weight_units, key="weight_from")
    with col2:
        to_unit = st.selectbox("To", weight_units, key="weight_to")
    value = st.number_input("Enter value", value=1.0, min_value=0.0, key="weight_value")
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif conversion_type == "Temperature":
    st.header("🌡️ Temperature Conversion")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", temp_units, key="temp_from")
    with col2:
        to_unit = st.selectbox("To", temp_units, key="temp_to")
    value = st.number_input("Enter value", value=0.0, key="temp_value")
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif conversion_type == "Volume":
    st.header("🧴 Volume Conversion")
    volume_units = ["Liters", "Milliliters", "Gallons", "Cubic Meters"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", volume_units, key="volume_from")
    with col2:
        to_unit = st.selectbox("To", volume_units, key="volume_to")
    value = st.number_input("Enter value", value=1.0, min_value=0.0, key="volume_value")
    result = convert_volume(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif conversion_type == "Area":
    st.header("📐 Area Conversion")
    area_units = ["Square Meters", "Square Feet", "Square Kilometers", "Hectares"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", area_units, key="area_from")
    with col2:
        to_unit = st.selectbox("To", area_units, key="area_to")
    value = st.number_input("Enter value", value=1.0, min_value=0.0, key="area_value")
    result = convert_area(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif conversion_type == "Speed":
    st.header("🚀 Speed Conversion")
    speed_units = ["Meters/Second", "Kilometers/Hour", "Miles/Hour", "Feet/Second"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", speed_units, key="speed_from")
    with col2:
        to_unit = st.selectbox("To", speed_units, key="speed_to")
    value = st.number_input("Enter value", value=1.0, min_value=0.0, key="speed_value")
    result = convert_speed(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif conversion_type == "Currency":
    st.header("💱 Currency Conversion")
    currency_units = ["USD", "EUR", "GBP", "JPY", "INR"]  
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", currency_units, key="currency_from")
    with col2:
        to_unit = st.selectbox("To", currency_units, key="currency_to")
    value = st.number_input("Enter value", value=1.0, min_value=0.0, key="currency_value")
    result = convert_currency(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif conversion_type == "Time":
    st.header("⏰ Time Conversion")
    time_units = ["Seconds", "Minutes", "Hours", "Days"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", time_units, key="time_from")
    with col2:
        to_unit = st.selectbox("To", time_units, key="time_to")
    value = st.number_input("Enter value", value=1.0, min_value=0.0, key="time_value")
    result = convert_time(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif conversion_type == "Energy":
    st.header("⚡ Energy Conversion")
    energy_units = ["Joules", "Calories", "Kilowatt-hours"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", energy_units, key="energy_from")
    with col2:
        to_unit = st.selectbox("To", energy_units, key="energy_to")
    value = st.number_input("Enter value", value=1.0, min_value=0.0, key="energy_value")
    result = convert_energy(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

# Reset button
if st.button("🔄 Reset"):
    st.experimental_rerun()

# Footer
st.markdown('<p class="stFooter">Created by Tayyeba Ali🖤</p>', unsafe_allow_html=True)