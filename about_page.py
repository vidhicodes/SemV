import streamlit as st

# Add this CSS block to each page
def apply_common_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
            color: #333;
        }

        .header-title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-top: 30px;
            color: #2C3E50;
        }

        .intro, .feature-title, .section-title {
            color: #1a1a1a;
        }

        .feature {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .feature:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }

        .stButton > button {
            background-color: #4caf50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
        }

        .stButton > button:hover {
            background-color: #388e3c;
            transform: scale(1.05);
        }

        .suggestion {
            background-color: #e0f7fa;
            border-radius: 8px;
            padding: 10px;
            margin-top: 10px;
        }

        .section-title {
            font-size: 26px;
            margin: 20px 0;
            font-weight: bold;
        }

        .contact-info, .footer {
            text-align: center;
            color: #555;
            font-size: 14px;
        }

        footer {
            text-align: center;
            padding: 20px;
            font-size: 14px;
            color: #777;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def show_about_page():
    apply_common_css()

    # Page content
    st.title("About This App")
    st.markdown("""
    Welcome to the **EcoSort** \n This tool utilizes cutting-edge machine learning to help users identify different types of waste and offers useful suggestions on recycling, reusing, and proper disposal.
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
        st.image("profile.png", caption="Vidhi Dhakate", use_column_width=True)
        st.markdown("**Vidhi Dhakate** \n Lead Developer")

    with col2:
         st.image("profile.png", caption="Tejas Mahakalkar", use_column_width=True)
         st.markdown("**Tejas Mahakalkar** \n Project Manager")

    with col3:
        st.image("profile.png", caption="Kashish Pawar", use_column_width=True)
        st.markdown("**Kashish Pawar** \n Data Scientist")

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
