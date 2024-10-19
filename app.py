import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page
from contact_page import show_contact_page  # Import the new contact page
from sustainability_page import show_sustainability_page  # Import the new sustainability page

# Custom CSS to style the app
def add_custom_css():
    st.markdown(
        """
        <style>
        /* General styles for the entire page */
        body {
            background-color: #EBF2B3;  /* Light background color from palette */
            font-family: 'Arial', sans-serif;  /* Basic font for the entire page */
            color: #1B4001;  /* Dark green text color */
        }

        /* Sidebar styles */
        .stSidebar {
            background-color: #1B4001;  /* Dark green background for the sidebar */
            color: white;  /* White text for better contrast */
        }

        .stSidebar .sidebar-title {
            font-size: 20px;  /* Make the sidebar title bigger */
            font-weight: bold;
            color: #EBF2B3;  /* Light background color for sidebar title */
            margin-bottom: 10px;
        }

        .stSidebar .widget-label {
            font-size: 16px;
            color: #EBF2B3;  /* Light text color */
        }

        /* Radio buttons in the sidebar */
        .stSidebar .radio {
            font-size: 16px;
            color: #EBF2B3;  /* Light text color for radio buttons */
            padding: 10px 0;
        }

        /* Add hover effect for sidebar navigation */
        .stSidebar .radio:hover {
            background-color: #3B7302;  /* Medium green hover effect */
            color: white;
        }

        /* Icons for the radio buttons */
        .stSidebar .radio:before {
            content: '🎯';  /* Add an icon */
            margin-right: 10px;
            font-size: 16px;
            color: white;
        }

        /* Styling for the main content area */
        .stApp {
            padding: 20px;
            background-color: #9BBF65;  /* Softer green for main content area */
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 1000px;
            margin: auto;
        }

        h1, h2, h3 {
            color: #1B4001;  /* Dark green for headers */
            font-weight: 600;
        }

        a {
            color: #65A603;  /* Medium green for links */
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
            color: #3B7302;  /* Darker green hover for links */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main function to navigate through the pages
def main():
    # Add custom CSS
    add_custom_css()

    # Set up the sidebar for navigation
    st.sidebar.title("Navigation")

    # Create radio buttons for navigation with icons
    page = st.sidebar.radio(
        "Go to:",
        ("🏠 Home", "🔍 Classification", "ℹ️ About", "✉️ Contact Us", "🌱 Sustainability Practices"),
        index=0,  # Default selected page
        label_visibility="collapsed"  # Hide the label for a cleaner look
    )

    # Call the corresponding page function based on the selected option
    if page == "🏠 Home":
        show_home_page()
    elif page == "🔍 Classification":
        show_classification_page()
    elif page == "ℹ️ About":
        show_about_page()
    elif page == "✉️ Contact Us":
        show_contact_page()    # Show the contact page
    elif page == "🌱 Sustainability Practices":
        show_sustainability_page()  # Show the sustainability practices page

if __name__ == "__main__":
    main()
