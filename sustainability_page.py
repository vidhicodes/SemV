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


# Show sustainability page with enhanced content
def show_sustainability_page():
    apply_common_css()
    
    st.title("Embrace Sustainability: Small Steps, Big Impact")
    
    st.markdown("### *Practical Ways to Live Sustainably*")
    
    st.markdown("""
    **1. Composting**:
    - Convert kitchen scraps and yard waste into nutrient-rich compost for your garden.
    - Reduces methane emissions from landfills and enriches soil naturally.
    - **Tip**: Use a compost bin or pile in your backyard, and avoid composting meat or dairy to prevent odors.

    **2. Water Conservation**:
    - Fix leaky faucets and install water-saving fixtures (like low-flow showerheads).
    - Collect rainwater for gardening or outdoor cleaning tasks.
    - **Tip**: Run dishwashers and washing machines with full loads to maximize water efficiency.

    **3. Energy Efficiency**:
    - Replace traditional bulbs with LED or CFL lights, which use less energy and last longer.
    - Invest in energy-efficient appliances and unplug devices when not in use to reduce 'phantom' energy consumption.
    - **Tip**: Use a smart power strip to turn off multiple devices at once.

    **4. Sustainable Transportation**:
    - Opt for public transportation, carpool, or biking whenever possible.
    - Reduce your carbon footprint by driving less, planning routes efficiently, or even switching to electric vehicles.
    - **Tip**: For short trips, consider walking or cycling – it's healthier and eco-friendly!

    **5. Mindful Consumption**:
    - Buy products with minimal packaging and choose items made from recycled or sustainable materials.
    - Support brands and companies that prioritize sustainability and ethical practices.
    - **Tip**: Bring your own reusable bags, bottles, and containers to reduce single-use plastic waste.
    
    ### *Get Involved and Make a Difference*
    
    **1. Participate in Community Events**:
    - Join local clean-up drives to help keep parks, beaches, and streets clean.
    - Support urban gardening initiatives and tree-planting events in your area.
    - **Tip**: Volunteer for or donate to local environmental organizations to amplify your impact.

    **2. Educate and Inspire Others**:
    - Spread awareness about the importance of recycling, reducing waste, and conserving energy.
    - Organize workshops or webinars to share knowledge on sustainable living practices.
    - **Tip**: Share your sustainability journey on social media to inspire friends and family.

    **3. Shop Local, Shop Green**:
    - Buy from local farmers' markets, thrift shops, or businesses that prioritize eco-friendly products.
    - Choose products that are organic, fair-trade, or sustainably sourced.
    - **Tip**: Reduce your carbon footprint by supporting local artisans and farmers who use sustainable practices.
    
    ### *Start Small, Think Big!*
    Remember, every small step counts towards a more sustainable future. Your efforts, no matter how small, can inspire a ripple effect of positive change!
    """)

show_sustainability_page()
