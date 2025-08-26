# Cac thu vien can su dung
import os
from PIL import Image

def load_image(image_path):
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print(f"Error: {e}")
        return None