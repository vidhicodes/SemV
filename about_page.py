import streamlit as st

def show_about_page():
    # Page content
    st.title("About EcoSort")
    st.markdown("""
    Welcome to the **EcoSort**.This tool utilizes cutting-edge machine learning to help users identify different types of waste and offers useful suggestions on recycling, reusing, and proper disposal.
    """)

    # Mission Section
    st.subheader("Our Mission")
    st.markdown("""
    Our mission is to encourage sustainable waste management practices by providing an easy-to-use tool that educates and empowers users to make better recycling choices. We believe that small actions can lead to significant environmental changes.
    """)

    # Team Section
    st.subheader("Meet the Team")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("profile.png", use_column_width=True)
        st.markdown("**Vidhi Dhakate** <br> Lead Developer", unsafe_allow_html=True)
    

    with col2:
         st.image("profile.png", use_column_width=True)
         st.markdown("**Tejas Mahakalkar** <br> Project Manager", unsafe_allow_html=True)

    with col3:
        st.image("profile.png", use_column_width=True)
        st.markdown("**Kashish Pawar** <br> Data Scientist", unsafe_allow_html=True)

    # Future Work Section
    st.subheader("Future Work")
   st.markdown("""
- **Real-Time Feedback**: Provide instant feedback on recycling efforts.
- **Expand Categories**: Add more waste categories for accurate identification.
- **Community Engagement**: Enable sharing of recycling tips and challenges.
- **Gamification**: Introduce rewards to boost user participation.
- **Educational Resources**: Offer articles on sustainability to enhance awareness.
""")


    # Call to Action Section
    st.subheader("Join Us")
    st.markdown("""
    Help make a positive impact! Share the app, join local clean-up efforts, and encourage others to adopt eco-friendly habits.
    """)

    st.markdown("### Thank you for supporting sustainable practices! Together, we can make a difference!")

show_about_page()
