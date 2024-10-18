import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page
from statistics_page import show_statistics_page  # Import the new statistics page
from faq_page import show_faq_page              # Import the new FAQ page
from contact_page import show_contact_page        # Import the new contact page
from sustainability_page import show_sustainability_page  # Import the new sustainability page

# Main function to navigate through the pages
def main():
    # Set up the sidebar for navigation
    st.sidebar.title("Navigation")
    
    # Create radio buttons for navigation with icons
    page = st.sidebar.radio(
        "Go to:",
        ("🏠 Home", "🔍 Classification", "ℹ️ About", "📊 Recycling Statistics", "❓ FAQ", "✉️ Contact Us", "🌱 Sustainability Practices"),
        index=0,  # Default selected page
        label_visibility="collapsed"  # Hide the label for a cleaner look
    )

    # Add descriptions for better user guidance
    st.sidebar.markdown(
        """
        Navigate through the application using the options above.
        - **Home:** Introduction to the Intelligent Waste Classification App.
        - **Classification:** Upload an image and classify your waste.
        - **About:** Learn more about the app and its development.
        - **Recycling Statistics:** Learn about recycling and its impact on the environment.
        - **FAQ:** Get answers to common questions about recycling and waste management.
        - **Contact Us:** Reach out for more information or support.
        - **Sustainability Practices:** Discover ways to live sustainably and reduce waste.
        """
    )

    # Call the corresponding page function based on the selected option
    if page == "🏠 Home":
        show_home_page()
    elif page == "🔍 Classification":
        show_classification_page()
    elif page == "ℹ️ About":
        show_about_page()
    elif page == "📊 Recycling Statistics":
        show_statistics_page()  # Show the statistics page
    elif page == "❓ FAQ":
        show_faq_page()        # Show the FAQ page
    elif page == "✉️ Contact Us":
        show_contact_page()    # Show the contact page
    elif page == "🌱 Sustainability Practices":
        show_sustainability_page()  # Show the sustainability practices page

if __name__ == "__main__":
    main()
