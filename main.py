import streamlit as st
import random
import string

def generate_password_meter(length ,use_digits  ,use_special):
    characters = string.ascii_letters


    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for loop in range(length))

st.title("Password Generator By Muhammad Ashhad Khan")

length = st.slider("Select Password Length", min_value=8 , max_value=20, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Use Special Characters")

if st.button("Generate Password"):
    password = generate_password_meter(use_digits  ,use_special)
    st.write(f"Generated Password: `{password}`")

    st.write("---------------------")

    st.write("Created By [Muhammad Ashhad Khan](https://github.com/Rukhsanaashhad)")
