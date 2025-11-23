import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI based BMI Calculator - Know your health!")

# BMI Calculator Inputs
name = st.text_input("Enter your name:")
wt = st.number_input("Enter your weight:")
ht = st.slider("Enter your height in cm:", 50, 250)
age = st.number_input("Enter your age:")
gender = st.text_input("Enter your gender:")

# Calculate BMI safely
if ht > 0 and wt > 0:
    bmi = round(wt / (ht / 100) ** 2, 2)
    st.write(f"{name}, your BMI is {bmi}")

    prompt = (
        f"Act like an expert nutritionist and comment on the BMI with the following data: "
        f"height {ht} cm, weight {wt} kg, age {age}, gender {gender}, BMI {bmi}"
    )

    # Generate content from Gemini
    response = model.generate_content(prompt)
    st.markdown(response.text)
else:
    st.write("Please enter valid height and weight.")
