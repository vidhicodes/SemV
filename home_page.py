import streamlit as st

# Add this CSS block to each page

def show_home_page():
    # Header
    st.markdown("<h1 class='header-title'>EcoSort 🌱</h1>", unsafe_allow_html=True)
    

    # Introduction Section
    st.markdown("<p class='intro'>This application helps you classify waste into different categories effortlessly. <br> Whether you are at home, at school, or in a business, understanding how to manage your waste is critical for a cleaner and greener environment. </p>", unsafe_allow_html=True)
    
    
    # Features Section
    st.subheader("Why Use This Application?")
    
    feature_list = [
        ("Accurate Classification", "Utilizes state-of-the-art machine learning models to accurately classify various waste types."),
        ("Instant Suggestions", "Receive instant suggestions on recycling, reusing, or disposing of waste responsibly."),
        ("Easy to Use", "Simply upload an image, and the app intelligently categorizes your waste."),
        ("Educational Resources", "Learn about waste management and how you can contribute to a sustainable future.")
    ]

    for title, description in feature_list:
        st.markdown(f"<div class='feature' onclick=\"alert('Feature: {title}')\"><div class='feature-title'>{title}</div><p>{description}</p></div>", unsafe_allow_html=True)

  
    # Footer
    st.markdown("<footer>Powered by Streamlit & Machine Learning</footer>", unsafe_allow_html=True)

