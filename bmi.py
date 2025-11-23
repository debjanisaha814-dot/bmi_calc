{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d156b03-53ca-4f36-a329-9953656c50d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import google.generativeai as genai\n",
    "import streamlit as st\n",
    "\n",
    "genai.configure(api_key=st.secrets[\"GOOGLE_API_KEY\"])\n",
    "\n",
    "# Initialize the model (Gemini 1.5 Turbo or Gemini Pro)\n",
    "model = genai.GenerativeModel(\"gemini-2.5-flash\")\n",
    "\n",
    "st.title(\"AI based BMI Calculator - Know your health!\")\n",
    "\n",
    "# BMI Calculator\n",
    "# Take inputs from the user\n",
    "name = st.text_input(\"Enter your name:\")\n",
    "wt = st.number_input(\"Enter your weight:\")\n",
    "ht = st.slider(\"Enter your height in cm:\",50,250)\n",
    "age = st.number_input(\"Enter your age:\")\n",
    "gender = st.text_input(\"Enter your gender:\")\n",
    "\n",
    "bmi = round(wt/(ht/100)**2,2)\n",
    "\n",
    "st.write(f\"{name}, your BMI is {bmi}\")\n",
    "\n",
    "prompt = f\"Act like an expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, age as {age}, gender as {gender} and BMI as {bmi}\"\n",
    "\n",
    "# Generate content from Gemini\n",
    "response = model.generate_content(prompt)\n",
    "\n",
    "st.markdown(response.text)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
