import streamlit as st

def show_contact_page():
    
    st.title("Contact Us")
    
    st.markdown("""
    If you have any questions, suggestions, or feedback, feel free to reach out to us!

    - **Vidhi Dhakate**: 
      - Email: dhakatevs@rknec.edu
      - Mobile: +91 9823299231

      <br>

    - **Tejas Mahakalkar**: 
      - Email: mahakalkarth@rknec.edu
      - Mobile: +91 7559137557

      <br>

    - **Kashish Pawar**: 
      - Email: pawarkn@rknec.edu
      - Mobile: +91 7049226830
    """, unsafe_allow_html=True)
