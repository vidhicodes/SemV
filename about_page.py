import streamlit as st

def show_about_page():
    # Apply background image style
    background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({background_image_url});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page content
    st.title("About This App")
    st.markdown("""
    Welcome to the **Intelligent Waste Classification App**! 🌍 This tool utilizes cutting-edge machine learning to help users identify different types of waste and offers useful suggestions on recycling, reusing, and proper disposal.
    """)

    # Mission Section
    st.subheader("Our Mission 🎯")
    st.markdown("""
    Our mission is to encourage sustainable waste management practices by providing an easy-to-use tool that educates and empowers users to make better recycling choices. We believe that small actions can lead to significant environmental changes.
    """)

    # Team Section
    st.subheader("Meet the Team 👥")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("profile.png", caption="Vidhi Dhakate", use_column_width=True)
        st.markdown("**Vidhi Dhakate**\nLead Developer")

    with col2:
         st.image("profile.png", caption="Tejas Mahakalkar", use_column_width=True)
         st.markdown("**Tejas Mahakalkar**\nProject Manager")

    with col3:
        st.image("profile.png", caption="Kashish Pawar", use_column_width=True)
        st.markdown("**Kashish Pawar**\nData Scientist")

    # Future Work Section
    st.subheader("Future Work 🚀")
    st.markdown("""
    - **Real-Time Feedback:** Allow users to receive instant feedback on their recycling practices.
    - **Expand Waste Categories:** Continue adding more waste categories for better identification.
    - **Community Features:** Enable users to share recycling tips and challenges.
    - **Gamification Elements:** Introduce badges and rewards for active participants to encourage engagement.
    - **Educational Resources:** Provide articles and resources on sustainability practices to enhance user knowledge.
    """)

    # Call to Action Section
    st.subheader("Get Involved! 🤝")
    st.markdown("""
    Join us in our mission to create a cleaner, greener planet! Here are some ways you can contribute:
    - **Spread the Word:** Share this app with friends and family to raise awareness about waste management.
    - **Participate in Local Clean-Up Events:** Get involved in your community and help keep your environment clean.
    - **Follow Us on Social Media:** Stay updated on our latest features and sustainability tips.
    """)

    st.success("Thank you for supporting sustainable practices! Together, we can make a difference!")
