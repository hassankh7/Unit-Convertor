# Bismillah

import streamlit as st

st.title("🌍 Unit Converter App")

st.markdown(" ### Converts Lenght And Weight And Time Instantly")
st.write("Welcome Select A Categoery, Enter A Value And Get The Converted Result In The Real Time ")


# Select category
category = st.selectbox("Select a category:", ["Length", "Weight", "Time"])

# Unit selection based on category
if category == "Length":
    unit = st.selectbox("Select a unit:", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select a unit:", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select a unit:", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Hours to Minutes", "Minutes to Hours",
        "Hours to Seconds", "Seconds to Hours"
    ])

# Value input
value = st.number_input("Enter a value to convert:", min_value=0.0, step=0.1)

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Seconds":
            return value * 3600
        elif unit == "Seconds to Hours":
            return value / 3600

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The converted value is: {result:.2f}")