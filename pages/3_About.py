import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="About - YOLO V5 Empty Chair Detection",
    layout="wide",
    page_icon="🪑"
)

# Custom CSS for styling
def apply_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #f7f7f5; /* Light beige background */
            color: #333; /* Darker text for readability */
        }
        h1, h2, h3, h4 {
            color: #4CAF50; /* Consistent green for titles */
        }
        .stMarkdown {
            font-size: 16px;
            line-height: 1.6; /* Better line spacing */
        }
        .highlight-box {
            background-color: #e8f5e9; /* Light green background */
            border-left: 4px solid #4CAF50; /* Green border */
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        .center-content {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

apply_custom_css()

# Page content
st.title("About YOLO V5 Empty Chair Detection 🪑")
st.markdown(
    """
    Welcome to the **YOLO V5 Empty Chair Detection App**!  
    This innovative web application leverages state-of-the-art AI technology to detect and count empty chairs in images and videos in real time. Whether you're managing events, optimizing seating arrangements, or conducting research, this tool offers a powerful solution.
    """
)

# Purpose section
st.header("🎯 Purpose of the App")
st.markdown(
    """
    - **Efficient Seating Management**: Quickly identify and count available chairs in large venues like conference rooms, auditoriums, or classrooms.
    - **Real-time Detection**: Use your webcam for live chair detection, perfect for dynamic environments.
    - **Versatile Use Cases**: From event planning to facility optimization, this app serves various industries.
    """
)

# Features section
st.header("✨ Key Features")
st.markdown(
    """
    - **Object Detection**: Detects empty chairs, people, and personal items in images or live video feeds.
    - **Webcam Integration**: Seamlessly integrates with your webcam for real-time detection.
    - **Easy to Use**: User-friendly interface that makes AI technology accessible to everyone.
    - **Accurate Results**: Powered by YOLO V5, one of the most advanced object detection models.
    """
)

# How it works section
st.header("🛠️ How It Works")
st.markdown(
    """
    1. **Upload an Image**: Provide an image of a room or environment.
    2. **Connect Your Webcam**: Use the webcam feature for real-time detection.
    3. **AI Processing**: Our advanced YOLO V5 model analyzes the image or video feed.
    4. **Results Displayed**: The number of empty chairs is counted and displayed instantly.
    """
)



# Footer with appreciation
st.markdown("---")
st.markdown(
    """
    <div class="center-content">
        Made with YOLO V5 and Streamlit.  
        Bringing AI solutions to your everyday challenges.
    </div>
    """,
    unsafe_allow_html=True,
)
