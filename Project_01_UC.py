import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Metre": 1,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Kilometre": 0.001,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors:
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])
    else:
        return None

st.title("Unit Converter")

category = st.selectbox("Select Category", ["Length"])

if category == "Length":
    from_unit = st.selectbox("From", ["Metre", "Centimetre", "Millimetre", "Kilometre", "Inch", "Foot", "Yard", "Mile"])
    to_unit = st.selectbox("To", ["Metre", "Centimetre", "Millimetre", "Kilometre", "Inch", "Foot", "Yard", "Mile"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.6f")
    
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
        else:
            st.error("Invalid conversion units selected.")
