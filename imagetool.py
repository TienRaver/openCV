# Cac thu vien can su dung
import os
from PIL import Image
# Func load anh
def load_image(image_path):
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print(f"Error: {e}")
        return None
#Func kiem tra anh
def image_checking(folder_path):
    extension = (".jpg",".png",".jpeg",".gif",".bmp")
    return folder_path.lower().endswith(extension)
#Func doc tat ca anh
def get_image_list(folder_path):
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames = os.listdir(folder_path)
        for filename in filenames:
            file_path = os.path.join(folder_path,filename)
            if os.path.isfile(folder_path) and image_checking(folder_path):
                img = load_image(image_path)
                image_list.append(img)
    return image_list