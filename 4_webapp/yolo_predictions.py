#!/usr/bin/env python
# coding: utf-8
import cv2
import numpy as np
import os
import yaml
from yaml.loader import SafeLoader


class YOLO_Pred:
    def __init__(self, onnx_model, data_yaml):
        # Load YAML
        with open(data_yaml, mode='r') as f:
            data_yaml = yaml.load(f, Loader=SafeLoader)

        self.labels = data_yaml['names']
        self.nc = data_yaml['nc']

        # Print all class labels (for debugging)
        print("Loaded class labels:", self.labels)

        # Load YOLO model
        self.yolo = cv2.dnn.readNetFromONNX(onnx_model)
        self.yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.yolo.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def predictions(self, image):
        row, col, d = image.shape

        # Convert image into a square array
        max_rc = max(row, col)
        input_image = np.zeros((max_rc, max_rc, 3), dtype=np.uint8)
        input_image[0:row, 0:col] = image

        # Prepare the image for YOLO
        INPUT_WH_YOLO = 640
        blob = cv2.dnn.blobFromImage(input_image, 1/255, (INPUT_WH_YOLO, INPUT_WH_YOLO), swapRB=True, crop=False)
        self.yolo.setInput(blob)
        preds = self.yolo.forward()

        # Filter detections based on confidence
        detections = preds[0]
        boxes = []
        confidences = []
        classes = []

        # Get dimensions of the input image
        image_w, image_h = input_image.shape[:2]
        x_factor = image_w / INPUT_WH_YOLO
        y_factor = image_h / INPUT_WH_YOLO

        for i in range(len(detections)):
            row = detections[i]
            confidence = row[4]
            if confidence > 0.4:  # Adjust confidence threshold if needed
                class_score = row[5:].max()
                class_id = row[5:].argmax()

                # Debug: Print detected classes
                print(f"Detected Class: {self.labels[class_id]}, Confidence: {confidence}")

                if class_score > 0.25:  # Adjust class score threshold if needed
                    cx, cy, w, h = row[0:4]
                    left = int((cx - 0.5 * w) * x_factor)
                    top = int((cy - 0.5 * h) * y_factor)
                    width = int(w * x_factor)
                    height = int(h * y_factor)

                    box = [left, top, width, height]
                    confidences.append(float(confidence))
                    boxes.append(box)
                    classes.append(class_id)

        # Non-Maximum Suppression
        boxes_np = np.array(boxes).tolist()
        confidences_np = np.array(confidences).tolist()
        indices = np.array(cv2.dnn.NMSBoxes(boxes_np, confidences_np, 0.25, 0.45)).flatten()

        # Count filtered "emptychair" objects
        empty_chair_count = 0

        # Draw bounding boxes and count "Empty Chair" detections
        for ind in indices:
            x, y, w, h = boxes_np[ind]
            bb_conf = int(confidences_np[ind] * 100)
            classes_id = classes[ind]
            class_name = self.labels[classes_id]

            # Highlight "Empty Chair" detections in green
            if class_name == "emptychair":
                empty_chair_count += 1
                colors = (0, 255, 0)  # Green for Empty Chair
            else:
                colors = self.generate_colors(classes_id)

            text = f'{class_name}: {bb_conf}%'
            cv2.rectangle(image, (x, y), (x + w, y + h), colors, 2)
            cv2.rectangle(image, (x, y - 30), (x + w, y), colors, -1)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 0), 1)

        # Debugging final count
        print(f"Final Empty Chair Count: {empty_chair_count}")

        # Return the processed image and the count of Empty Chair objects
        return image, empty_chair_count


    def generate_colors(self, ID):
        np.random.seed(10)
        colors = np.random.randint(100, 255, size=(self.nc, 3)).tolist()
        return tuple(colors[ID])
