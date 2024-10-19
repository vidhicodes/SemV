import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page
from contact_page import show_contact_page        # Import the new contact page
from sustainability_page import show_sustainability_page  # Import the new sustainability page

# Main function to navigate through the pages
def main():
    # Set up the sidebar for navigation
    st.sidebar.title("EcoSort")
    
    # Create radio buttons for navigation with icons
    page = st.sidebar.radio(
        "Go to:",
        ("Home", "Classification", "About","Contact Us", "Sustainability Practices"),
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
