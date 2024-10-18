import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page

# Initialize the session state if not set
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Navigation logic
if st.session_state['page'] == 'home':
    show_home_page()
elif st.session_state['page'] == 'classification':
    show_classification_page()
