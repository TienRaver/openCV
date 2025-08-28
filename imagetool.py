# Nhap cac thu vien can thiet
import os
from PIL import Image
from IPython.display import display
# Func 1: Mo mot anh bat ky
def OpenImage(image_path):
    image = Image.open(image_path)
    print(image.size)
    image.show()
    image.close()
# Func 2: Mo tat ca anh trong thu muc
def OpenImages(folder_path):
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
               image.show()
               image.close()
        return image_list # Tra ve toan bo anh
    # Goi tat ca func tren ra
    CheckFolder(folder_path)
    CheckImage_Extension(folder_path)
    LoadImage(folder_path)

# Func 3: Resize anh
def resize(folder_path,image_path):
    image = Image.open(image_path)
    # Kich thuoc anh moi
    newsize = (int(input("New width: ")),
               int(input("New height: "))) 
    print(f"New size : {newsize}")
    new_image = image.resize(newsize) # Thay doi kich thuoc anh
    new_image.show()
    try:
        new_name = input("New image name: ")
        # Them dinh dang anh tu dong
        extension = image.format.lower()
        if not new_name.lower().endswith(f".{extension}"):
            new_name += f".{extension}"
        save_path = os.path.join(folder_path,new_name) # Dia chi luu anh moi
        new_image.save(save_path,format=image.format,quality=100) # Luu anh moi
        print("Save new image successfully")
    except Exception as e:
        print(f"Error: {e}")
    image.close()
# Func 4: Thumbnail anh
def thumbnail(folder_path,image_path):
    image = Image.open(image_path)
    # Nhap kich thuoc toi da cho phep
    newsize = (int(input("Max width: ")),
               int(input("Max height: ")))
    print(f"Max size: {newsize}")
    image.thumbnail(newsize) # Thumbnail
    image.show()
    # Them dinh dang anh tu dong
    extension = image.format.lower()
    new_name = input("New image name: ")
    if not new_name.lower().endswith(f".{extension}"):
        new_name += f".{extension}"
    # Luu anh moi
    new_path = os.path.join(folder_path,new_name)
    image.save(new_path,format=image.format,quality=100)
    print("Copied new image successfully")
    image.close()