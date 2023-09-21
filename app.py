import streamlit as st
import random

st.markdown("<h1 style='text-align: center;'>🔑Safety Password Generator</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Crafted by Izatcrust ✨</p>", unsafe_allow_html=True)
st.divider()

char_set_1 = '~!@#$%^&*()_+-=,./<>?;":[]\{}|'
char_set_1_mobile_friendly = '!@#$%^&*()'
char_set_2 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

col1, col2 = st.columns(2)

with col1:
    is_mobile = st.checkbox('Mobile Friendly', value=True)
    length = st.slider('Password Length', min_value=8, max_value=20)
    
with col2:
    chosen_set = char_set_1_mobile_friendly if is_mobile else char_set_1
    char_set_1 = st.text_input('Specials', value=chosen_set)
    char_set_2 = st.text_input('Numbers and Letters', value=char_set_2)

password_space = char_set_1 + char_set_2

def generate_password(space, length):
    for _ in range(length):
        yield random.SystemRandom().choice(space)

col3, col4, = st.columns(2)

with col3:
    st.button("Generate Password")

with col4:
    st.code(''.join(generate_password(password_space, length)))
    st.markdown("<p style='text-align: right;'>Copy Password 👆</p>", unsafe_allow_html=True)