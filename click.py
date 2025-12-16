import streamlit as st
import os
import cv2
from PIL import Image
import numpy as np

PERSON_NAME = "person_01"
TOTAL_IMAGES = 100

SAVE_DIR = os.path.join("dataset", PERSON_NAME)
os.makedirs(SAVE_DIR, exist_ok=True)

st.title("Face Dataset Capture")
st.write(f"Capture {TOTAL_IMAGES} images")

count = len(os.listdir(SAVE_DIR))

img_file = st.camera_input("Take a picture")

if img_file is not None and count < TOTAL_IMAGES:
    image = Image.open(img_file)
    img_np = np.array(image)

    filename = f"img_{count+1:03d}.jpg"
    cv2.imwrite(os.path.join(SAVE_DIR, filename), img_np)

    st.success(f"Saved {filename} ({count+1}/{TOTAL_IMAGES})")
    st.image(image)

if count >= TOTAL_IMAGES:
    st.success("✅ 100 images captured!")
