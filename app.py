import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page
from contact_page import show_contact_page        # Import the new contact page
from sustainability_page import show_sustainability_page  # Import the new sustainability page
import streamlit as st

def apply_common_css():
    st.markdown("""
    <style>
    /* Common Styles */
    .stApp {
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        font-family: 'Arial', sans-serif;
    }
    
    body {
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        color: #fff;
    }

    /* Home Page Styles */
    .header-title {
            text-align: center;
            font-size: 3.5em;
            color: 	#00A86B; /* Green shade for eco-friendliness */
            font-weight: 700;
            padding: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }

    .intro {
        font-size: 22px;
        text-align: center;
        margin: 20px auto;
        max-width: 800px;
        animation: slideIn 1s;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    .feature {
        background-color: #00A86B;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s, box-shadow 0.3s;
        cursor: pointer;
    }

    .feature:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 30px rgba(0, 0, 0, 0.25);
    }

    .feature-title {
        font-weight: bold;
        color: #ffffc5;
        font-size: 24px;
        margin-bottom: 10px;
    }

    /* Classification Page Styles */
    .title {
        text-align: center;
        font-size: 2.5em;
        color: #fff;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
    }

    .button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.2em;
        transition: background-color 0.3s ease;
    }

    .button:hover {
        background-color: #45a049;
    }

    .suggestion {
        background-color: #00A86B;
        border-radius: 8px;
        padding: 10px;
        margin-top: 10px;
    }

    /* Sustainability Page Styles */
    .stats-container {
        text-align: center;
        margin: 40px 0;
        animation: bounceIn 1s;
    }

    @keyframes bounceIn {
        0% { transform: scale(0); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    /* Footer */
    footer {
        text-align: center;
        padding: 20px;
        font-size: 14px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)


# Main function to navigate through the pages
def main():
    apply_common_css()  # Apply common CSS styles

    # Set up the sidebar for navigation
    st.sidebar.title("EcoSort 🌱")
    
    # Create radio buttons for navigation with icons
    page = st.sidebar.radio(
        "Go to:",
        ("Home", "Classification", "Sustainability Practices", "About", "Contact Us"),
        index=0,  # Default selected page
        label_visibility="collapsed"  # Hide the label for a cleaner look
    )

    # Call the corresponding page function based on the selected option
    if page == "Home":
        show_home_page()
    elif page == "Classification":
        show_classification_page()
    elif page == "About":
        show_about_page()
    elif page == "Contact Us":
        show_contact_page()    # Show the contact page
    elif page == "Sustainability Practices":
        show_sustainability_page()  # Show the sustainability practices page

if __name__ == "__main__":
    main()
