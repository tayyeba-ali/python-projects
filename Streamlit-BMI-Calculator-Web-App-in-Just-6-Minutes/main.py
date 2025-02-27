import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height in meters(e.g., 1.75):", min_value =0.0, format ="%.2f")
weight = st.number_input("Enter your weight in kilograms(e.g., 70):", min_value =0.0, format ="%.2f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0 :
        bmi = weight / (height ** 2)
        st.success(f"You BMI is : {bmi:.2f}")


        if bmi < 18.5:
            st.info("You are underweight")
        elif 18.5 <= bmi < 24.0:
            st.success("You have a normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight ")  
        else:      
            st.error("You are obses")
    else:
        st.error("Please enter valid height and weight")
        
        



        