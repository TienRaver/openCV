# Import library
import os
from PIL import Image
from IPython.display import display
# Func 1: Open any image
def OpenImage(image_path):
    image = Image.open(image_path)
    print(image.size)
    image.show()
    image.close()
# Func 2: Open all images in a folder
def OpenImages(folder_path):
    # Func check folder exist
    def CheckFolder(folder_path):
        try:
            return os.path.exists(folder_path)
        except Exception as e:
            print(f"Error folder: {e}")
    # Func check image exist in a folder
    def CheckImage_Extension(folder_path):
        try:
            extension = (".jpg",".png",".tiff",".gif",".bmp",".raw")
            extension_checking = folder_path.lower().endswith(extension) # check image format
            return extension_checking
        except Exception as e:
            print(f"Error image extension: {e}")    
    # Func open all images in a folder
    def LoadImage(folder_path):
        image_list = []
        filenames = os.listdir(folder_path) # List all filenames in a folder
        # In tat ca anh
        for filename in filenames:
            if os.path.isfile(folder_path+"/"+filename): # check is file or not
               image = Image.open(folder_path+"/"+filename) # Open image path
               image_list.append(image) # Add image in list
               image.show()
               image.close()
        return image_list # return all images
    # Call all above func
    CheckFolder(folder_path)
    CheckImage_Extension(folder_path)
    LoadImage(folder_path)

# Func 3: Resize image
def resize(folder_path,image_path):
    image = Image.open(image_path)
    # New size
    newsize = (int(input("New width: ")),
               int(input("New height: "))) 
    print(f"New size : {newsize}")
    new_image = image.resize(newsize) # Change image size
    new_image.show()
    try:
        new_name = input("New image name: ")
        # Add image extension automatically
        extension = image.format.lower()
        if not new_name.lower().endswith(f".{extension}"):
            new_name += f".{extension}"
        save_path = os.path.join(folder_path,new_name) # New path
        new_image.save(save_path,format=image.format,quality=100) # Save new image
        print("Save new image successfully")
    except Exception as e:
        print(f"Error: {e}")
    image.close()
# Func 4: Thumbnail
def thumbnail(folder_path,image_path):
    image = Image.open(image_path)
    # Max image size
    newsize = (int(input("Max width: ")),
               int(input("Max height: ")))
    print(f"Max size: {newsize}")
    image.thumbnail(newsize) # Thumbnail
    image.show()
    # Add image extension automatically
    extension = image.format.lower()
    new_name = input("New image name: ")
    if not new_name.lower().endswith(f".{extension}"):
        new_name += f".{extension}"
    # Save new image
    new_path = os.path.join(folder_path,new_name)
    image.save(new_path,format=image.format,quality=100)
    print("Copied new image successfully")
    image.close()