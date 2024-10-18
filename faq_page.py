import streamlit as st

def show_faq_page():
    st.title("❓ Frequently Asked Questions")

    st.markdown("""
    ### Common Questions About Recycling
    
    **Q: What types of materials can be recycled?**  
    A: Most common recyclable materials include paper, cardboard, glass, metals, and certain plastics. Always check local guidelines.

    **Q: How should I prepare items for recycling?**  
    A: Rinse containers to remove food residue, flatten boxes, and sort materials as needed by your local recycling program.

    **Q: What happens to items after they are recycled?**  
    A: Recycled materials are processed and transformed into new products, helping to conserve resources and reduce waste.

    **Q: Can I recycle plastic bags?**  
    A: Many curbside recycling programs do not accept plastic bags. Check local stores, as many have designated bins for plastic bag recycling.
    """)
