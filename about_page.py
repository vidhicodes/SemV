import streamlit as st

def show_about_page():
    # Page content
    st.title("About EcoSort")
    st.markdown("
    Welcome to the **EcoSort** <br> This tool utilizes cutting-edge machine learning to help users identify different types of waste and offers useful suggestions on recycling, reusing, and proper disposal.
    ", unsafe_allow_html=True)

    # Mission Section
    st.subheader("Our Mission")
    st.markdown("""
    Our mission is to encourage sustainable waste management practices by providing an easy-to-use tool that educates and empowers users to make better recycling choices. We believe that small actions can lead to significant environmental changes.
    """)

    # Team Section
    st.subheader("Meet the Team")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("profile.png", caption="Vidhi Dhakate", use_column_width=True)
        st.markdown("**Vidhi Dhakate** <br> Lead Developer", unsafe_allow_html=True)
    

    with col2:
         st.image("profile.png", caption="Tejas Mahakalkar", use_column_width=True)
         st.markdown("**Tejas Mahakalkar** <br> Project Manager", unsafe_allow_html=True)

    with col3:
        st.image("profile.png", caption="Kashish Pawar", use_column_width=True)
        st.markdown("**Kashish Pawar** <br> Data Scientist", unsafe_allow_html=True)

    # Future Work Section
    st.subheader("Future Work")
    st.markdown("""
    - **Real-Time Feedback:** Allow users to receive instant feedback on their recycling practices.
    - **Expand Waste Categories:** Continue adding more waste categories for better identification.
    - **Community Features:** Enable users to share recycling tips and challenges.
    - **Gamification Elements:** Introduce badges and rewards for active participants to encourage engagement.
    - **Educational Resources:** Provide articles and resources on sustainability practices to enhance user knowledge.
    """)

    # Call to Action Section
    st.subheader("Join Us")
    st.markdown("""
    Join us in our mission to create a cleaner, greener planet! Here are some ways you can contribute:
    - **Spread the Word:** Share this app with friends and family to raise awareness about waste management.
    - **Participate in Local Clean-Up Events:** Get involved in your community and help keep your environment clean.
    - **Follow Us on Social Media:** Stay updated on our latest features and sustainability tips.
    """)

    st.success("Thank you for supporting sustainable practices! Together, we can make a difference!")
