import cv2
import streamlit as st
from yolo_predictions import YOLO_Pred

# Load YOLO model
yolo = YOLO_Pred('./models/best.onnx', './models/data.yaml')

# Streamlit components
st.title("YOLO V5 Object Detection with Webcam")
st.markdown("Real-time detection and counting of empty chairs using your webcam.")

# Placeholder for video feed and empty chair count
video_placeholder = st.empty()
empty_chair_placeholder = st.empty()

# "Stop Webcam" button with a unique key
stop_button = st.button("Stop Webcam", key="stop_button")

# Start webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam
if not cap.isOpened():
    st.error("Error: Could not access the webcam. Please check your webcam connection.")
else:
    while not stop_button:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Failed to read video frame. Exiting...")
            break

        # Get predictions and empty chair count
        pred_img, empty_chair_count = yolo.predictions(frame)

        # Convert the processed frame (with bounding boxes) to RGB
        pred_img_rgb = cv2.cvtColor(pred_img, cv2.COLOR_BGR2RGB)

        # Display video feed
        video_placeholder.image(pred_img_rgb, channels="RGB", use_column_width=True)

        # Update empty chair count
        empty_chair_placeholder.markdown(
            f"### Number of Empty Chairs Detected: **{empty_chair_count}**"
        )

    # Cleanup after the loop
    cap.release()
    cv2.destroyAllWindows()
    st.success("Webcam stopped successfully!")
