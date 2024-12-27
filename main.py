import streamlit as st

# Title of the app
st.title("Addition of Two Numbers")

# Input fields for the two numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Button to calculate the sum
if st.button("Calculate"):
    result = num1 + num2
    st.success(f"The sum of {num1} and {num2} is {result}.")
