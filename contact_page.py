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


def show_contact_page():
    apply_common_css()
    
    st.title("Contact Us")
    
    st.markdown("""
    If you have any questions, suggestions, or feedback, feel free to reach out to us!

    - **Email**: contact@example.com
    - **Phone**: +1 (555) 123-4567
    - **Follow us on Social Media**:
      - [Facebook](https://facebook.com)
      - [Twitter](https://twitter.com)
      - [Instagram](https://instagram.com)
    """)
