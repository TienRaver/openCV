# Nhap cac thu vien can thiet
import os
from PIL import Image
from IPython.display import display
# Func mo tat ca cac anh
def OpenImage(folder_path):
    # Func kiem tra su ton tai cua thu muc
    def CheckFolder(folder_path):
        try:
            return os.path.exists(folder_path)
        except Exception as e:
            print(f"Error folder: {e}")
    # Func kiem tra su ton tai cua anh trong thu muc
    def CheckImage_Extension(folder_path):
        try:
            extension = (".jpg",".png",".tiff",".gif",".bmp",".raw")
            extension_checking = folder_path.lower().endswith(extension) # Kiem tra dinh dang anh
            return extension_checking
        except Exception as e:
            print(f"Error image extension: {e}")    
    # Func mo tat ca anh trong thu muc
    def LoadImage(folder_path):
        image_list = []
        filenames = os.listdir(folder_path) # Liet ke tat ca ten file trong thu muc
        # In tat ca anh
        for filename in filenames:
            if os.path.isfile(folder_path+"/"+filename): # Kiem tra la file hay khong
               image = Image.open(folder_path+"/"+filename) # Mo duong dan
               image_list.append(image) # Them anh vao list
               print(image.size)
               display(image) # Mo anh
               image.close()
        return image_list # Tra ve toan bo anh
    CheckFolder(folder_path)
    CheckImage_Extension(folder_path)
    LoadImage(folder_path)
OpenImage(str(input("Enter path: ")))


