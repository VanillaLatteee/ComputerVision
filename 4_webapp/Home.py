import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Empty Seat Detection",
    layout="wide",
    page_icon="🪑"
)

# Header section
st.title("YOLO V5 Empty Seat Detection App")
st.caption("Easily detect empty seats using advanced AI technology")

# Introduction
st.markdown(
    """
    Welcome to the **YOLO V5 Empty Seat Detection App**.  
    Our app is designed to help identify and count empty seats in any image for better seating management.
    """
)

# Navigation to Detection Page
with st.container():
    st.markdown("### Start Detecting Now")
    st.markdown(
        """
        Click the button below to upload an image and get real-time detection results:
        """
    )
    st.markdown(
        """
        <a href="http://localhost:8501/YOLO_for_image" target="_self">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; 
                           text-align: center; text-decoration: none; display: inline-block; 
                           font-size: 16px; border: none; border-radius: 5px; cursor: pointer;">
                Go to Detection Page
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# Features Section
st.markdown("---")
st.markdown("### What Our App Can Do")
st.write(
    """
    - **Detect Empty Seats**: Automatically identify and count the number of empty seats in an image.
    - **Person Detection**: Identify individuals in an image for better management insights.
    - **Personal Items Detection**: Detect and categorize objects left on seats.
    """
)

# Footer
st.markdown("---")
st.caption("Powered by YOLO V5 | Optimized for seating management use cases")
