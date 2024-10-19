import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page
from contact_page import show_contact_page        # Import the new contact page
from sustainability_page import show_sustainability_page  # Import the new sustainability page

def apply_common_css():
    css = """
    <style>
        body {
            background-color: #1e1e1e; /* Dark background */
            color: #ffffff; /* Light text color */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #f0f0f0; /* Slightly lighter text for headings */
        }
        .stButton {
            background-color: #0072b1; /* Button color */
            color: white; /* Button text color */
            border: none; /* Remove border */
            border-radius: 5px; /* Rounded corners */
            padding: 10px 20px; /* Padding for buttons */
            transition: background-color 0.3s; /* Smooth background transition */
        }
        .stButton:hover {
            background-color: #005580; /* Darker shade on hover */
        }
        .stTextInput, .stTextArea {
            background-color: #2b2b2b; /* Dark background for text input */
            color: #ffffff; /* Light text color */
            border: 1px solid #444; /* Border for input fields */
            border-radius: 5px; /* Rounded corners for input fields */
        }
        .stTextInput:focus, .stTextArea:focus {
            border-color: #0072b1; /* Change border color on focus */
            outline: none; /* Remove default outline */
        }
        .stMarkdown {
            color: #f0f0f0; /* Light text color for markdown */
        }
        .stSelectbox, .stMultiselect {
            background-color: #2b2b2b; /* Dark background for select boxes */
            color: #ffffff; /* Light text color */
            border: 1px solid #444; /* Border for select boxes */
            border-radius: 5px; /* Rounded corners for select boxes */
        }
        .stSelectbox:focus, .stMultiselect:focus {
            border-color: #0072b1; /* Change border color on focus */
            outline: none; /* Remove default outline */
        }
        .stSlider {
            color: #0072b1; /* Slider color */
        }
        .stAlert {
            background-color: #2b2b2b; /* Background for alerts */
            color: #ffffff; /* Text color for alerts */
            border-left: 4px solid #0072b1; /* Left border for alerts */
        }
        .stMarkdown img {
            max-width: 100%; /* Responsive images */
            height: auto; /* Maintain aspect ratio */
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Main function to navigate through the pages
def main():
    apply_common_css()  # Apply common CSS styles

    # Set up the sidebar for navigation
    st.sidebar.title("EcoSort")
    
    # Create radio buttons for navigation with icons
    page = st.sidebar.radio(
        "Go to:",
        ("Home", "Classification", "About", "Contact Us", "Sustainability Practices"),
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
