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


def show_home_page():
    apply_common_css()
    # Header
    st.markdown("<h1 class='header-title'>Ecosort</h1>", unsafe_allow_html=True)
    

    # Introduction Section
    st.markdown("<p class='intro'>**This application helps you classify waste into different categories effortlessly.**</p>", unsafe_allow_html=True)
    st.markdown("<p class='intro'>Whether you are at home, at school, or in a business, understanding how to manage your waste is critical for a cleaner and greener environment.</p>", unsafe_allow_html=True)

    # Call to Action Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Get Started", key="get_started"):
            st.markdown(
                "<script>window.location.href = '/classification_page';</script>",
                unsafe_allow_html=True
            )

    with col2:
        if st.button("Learn More", key="learn_more"):
            st.markdown(
                "<script>window.location.href = '/about_page';</script>",
                unsafe_allow_html=True
            )

    # Features Section
    st.subheader("Why Use This Application?")
    
    feature_list = [
        ("Accurate Classification", "Utilizes state-of-the-art machine learning models to accurately classify various waste types."),
        ("Real-Time Suggestions", "Receive instant suggestions on recycling, reusing, or disposing of waste responsibly."),
        ("Easy to Use", "Simply upload an image, and the app intelligently categorizes your waste."),
        ("Educational Resources", "Learn about waste management and how you can contribute to a sustainable future.")
    ]

    for title, description in feature_list:
        st.markdown(f"<div class='feature' onclick=\"alert('Feature: {title}')\"><div class='feature-title'>{title}</div><p>{description}</p></div>", unsafe_allow_html=True)

  
    # Footer
    st.markdown("<footer>Powered by Streamlit & Machine Learning</footer>", unsafe_allow_html=True)

