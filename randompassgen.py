import streamlit as st
import string
import random

st.title("Random Password Generator")

# Getting password length
length = st.slider("Choose password length:", 1, 50, 8)

character_sets = {
    "Digits": string.digits,
    "Letters": string.ascii_letters,
    "Special characters": string.punctuation,
}

selected_character_sets = st.multiselect("Choose character sets for password:", list(character_sets.keys()))

characterList = ""
for character_set in selected_character_sets:
    characterList += character_sets[character_set]

if st.button("Generate Password"):
    if not characterList:
        st.warning("Please select at least one character set for the password.")
    else:
        password = ''.join(random.choice(characterList) for i in range(length))
        st.success(f"Generated Password: {password}")
