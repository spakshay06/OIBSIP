import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

st.title("BMI Calculator")
weight = st.number_input("Enter your weight in kilograms", min_value=0.1)
height = st.number_input("Enter your height in meters", min_value=0.1)

if st.button("Calculate BMI"):
    if weight <= 0 or height <= 0:
        st.error("Invalid input. Please enter positive values for weight and height.")
    else:
        bmi = calculate_bmi(weight, height)
        st.info("Your BMI is: {:.2f}".format(bmi))
        if bmi < 18.5:
            st.warning("You are Underweight!", icon="⚠️")
        elif bmi>=18.5 and bmi <24.9:
            st.success("You are Healthy!", icon ="✅")
        elif bmi>=24.9 and bmi<29.9:
            st.warning("You are Overweight!", icon="⚠️")
        else:
            st.warning("You are Obese!", icon="🚨")


