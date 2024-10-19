import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page
from contact_page import show_contact_page        # Import the new contact page
from sustainability_page import show_sustainability_page  # Import the new sustainability page

# Function to apply common CSS styles
def apply_common_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #1E1E1E;  /* Main background for dark mode */
            color: #F1F1F1;  /* Main text color */
        }

        .sidebar {
            background-color: #2A2A2A;  /* Darker background for the sidebar */
            color: white;  /* Text color for sidebar */
        }

        h1, h2, h3, h4 {
            color: #F1F1F1;  /* Title color */
            font-weight: bold;  /* Bolder title text */
        }

        button {
            background-color: #4CAF50;  /* Button background */
            color: white;  /* Button text color */
            border: none;  /* Remove borders */
            padding: 10px;  /* Padding for buttons */
            border-radius: 5px;  /* Rounded corners for buttons */
            cursor: pointer;  /* Pointer cursor for buttons */
        }

        button:hover {
            background-color: #45a049;  /* Darker shade on hover */
        }

        .stTextInput, .stTextArea {
            background-color: #2A2A2A;  /* Dark background for text inputs */
            color: #F1F1F1;  /* Text color for inputs */
            border: 1px solid #4CAF50;  /* Green border for inputs */
            border-radius: 5px;  /* Rounded corners */
            padding: 8px;  /* Padding for inputs */
        }

        .stTextInput:focus, .stTextArea:focus {
            border-color: #8BC34A;  /* Lighter border on focus */
            outline: none;  /* Remove default outline */
        }

        .stButton > button {
            transition: background-color 0.3s;  /* Smooth transition for button hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

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
