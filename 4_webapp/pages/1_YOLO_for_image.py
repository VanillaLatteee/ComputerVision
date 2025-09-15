import streamlit as st
from yolo_predictions import YOLO_Pred
from PIL import Image
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="YOLO Object Detection",
    layout="wide",
    page_icon="🖼️"
)

# Custom CSS for styling
def apply_custom_css():
    st.markdown(
        """
        <style>
        /* General body settings */
        body {
            background-color: #f5f5f5; /* Light gray background */
            coloimr: #333; /* Darker text for readability */
        }
        .stButton > button {
            background-color: #4CAF50; /* Green button */
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
        }
        .stButton > button:hover {
            background-color: #45a049; /* Darker green on hover */
        }
        .stImage > img {
            border-radius: 10px;
        }
        h1, h2, h3, h4 {
            color: #4CAF50; /* Consistent green theme for headers */
        }
        .stSpinner {
            color: #4CAF50; /* Green spinner for loading */
        }
        .stInfo {
            background-color: #e8f5e9; /* Light green info box */
            border-left: 4px solid #4CAF50;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_custom_css()

# Header Section
st.title("🎯 YOLO V5 Object Detection App")
st.caption("Upload your images to detect objects like empty seats, people, and personal items.")

# Upload Image Section
with st.container():
    st.markdown("### Upload Image")
    st.write("Select an image to start detecting objects.")
    image_file = st.file_uploader("Upload Image (PNG or JPEG)", type=["png", "jpg", "jpeg"])

# Load YOLO model
with st.spinner("Loading YOLO model..."):
    yolo = YOLO_Pred(onnx_model="./models/best.onnx", data_yaml="./models/data.yaml")

# Main logic
if image_file:
    # Display uploaded image preview
    image_obj = Image.open(image_file)
    st.image(image_obj, caption="Uploaded Image Preview", use_column_width=True)

    # Detection button
    if st.button("Run Detection"):
        with st.spinner("Processing image, please wait..."):
            # Convert image to numpy array
            image_array = np.array(image_obj)
            pred_img, empty_chair_count = yolo.predictions(image_array)
            pred_img_obj = Image.fromarray(pred_img)

        # Display results
        st.markdown("### Detection Results")
        col1, col2 = st.columns(2)

        with col1:
            st.image(pred_img_obj, caption="Detected Image", use_column_width=True)
        
        with col2:
            st.info(f"Number of Empty Chairs Detected: {empty_chair_count}")
else:
    st.info("Please upload an image to proceed.")
