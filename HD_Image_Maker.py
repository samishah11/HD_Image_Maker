import streamlit as st
from PIL import Image
import io
import cv2
import numpy as np

def upscale_image(image, scale):
    # Convert image to OpenCV format
    img_cv = np.array(image)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    
    # Get new dimensions
    width = int(img_cv.shape[1] * scale / 100)
    height = int(img_cv.shape[0] * scale / 100)
    
    # Upscale image
    upscaled_img = cv2.resize(img_cv, (width, height), interpolation=cv2.INTER_CUBIC)
    
    # Convert back to PIL format
    upscaled_pil = Image.fromarray(cv2.cvtColor(upscaled_img, cv2.COLOR_BGR2RGB))
    return upscaled_pil

st.title("Image Upscaler: Enhance Resolution with Custom Scaling")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    scale = st.slider("Select Upscale Percentage", min_value=0, max_value=1000, value=50, step=200)
    
    if st.button("Upscale Image"):
        upscaled_image = upscale_image(image, scale)
        st.image(upscaled_image, caption=f"Upscaled Image ({scale}%)", use_container_width=True)
        
        # Convert image to bytes for download
        img_bytes = io.BytesIO()
        upscaled_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        st.download_button(label="Download Upscaled Image", data=img_bytes, file_name="upscaled_image.png", mime="image/png")
