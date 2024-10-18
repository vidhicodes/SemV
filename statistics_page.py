import streamlit as st

def show_statistics_page():
    # Apply background image style
    background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({background_image_url});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page content
    st.title("📊 Recycling Statistics")

    st.markdown("""
    ### 🌍 The Importance of Recycling
    Recycling is a vital component of environmental sustainability. It reduces the strain on our planet by cutting down on waste, conserving resources, and reducing pollution. Here are some eye-opening statistics:
    
    - ♻️ **Global Recycling Rate**: Currently, only about **13%** of the world's plastic is recycled. This highlights the need for increased recycling efforts and better waste management systems.
    - ⚡ **Energy Savings**: Recycling aluminum saves up to **95%** of the energy compared to producing new aluminum from raw materials. This can lead to significant reductions in greenhouse gas emissions.
    - 🌱 **Reduction in Landfill Waste**: Recycling and composting prevented the release of approximately **186 million metric tons** of carbon dioxide equivalent into the atmosphere in 2018, showing how small actions can lead to big changes.

    ### 🌟 Benefits of Recycling
    - **Conserves Natural Resources**: Each recycled product means fewer raw materials are extracted from the earth, helping to preserve ecosystems and wildlife.
    - **Saves Energy**: Making products from recycled materials uses less energy compared to manufacturing from new raw resources, reducing energy consumption and pollution.
    - **Reduces Pollution**: Recycling cuts down on emissions from waste incineration and the need for new raw materials, helping to combat air and water pollution.

    ### 🏆 How You Can Make a Difference
    - **Reduce**: 
        - 🌿 Buy products with minimal or no packaging.
        - 🛍️ Use reusable shopping bags, bottles, and containers.
    - **Reuse**: 
        - ♻️ Repurpose jars, cans, and containers instead of throwing them away.
        - 🎨 Get creative! Use old items for DIY projects or donate them to charity.
    - **Recycle**: 
        - 🗑️ Follow your local recycling guidelines to ensure materials are correctly sorted.
        - ✅ Check for recycling symbols on packaging and educate yourself on what can and cannot be recycled.
    
    ### 🤝 Community Involvement
    - **Join Local Initiatives**: Participate in neighborhood clean-ups and recycling drives.
    - **Spread Awareness**: Educate your community about the importance of recycling and how to do it properly.
    - **Support Eco-friendly Brands**: Choose brands that prioritize sustainable packaging and ethical practices.
    """)
