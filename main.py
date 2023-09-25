import streamlit as st

st.header('st.button')

if st.button('안녕'):
     st.write('왜 거기 있어')
else:
     st.write('Goodbye')