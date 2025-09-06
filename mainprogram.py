from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib_tool

image_folder = input("Image folder: ")
image_folder = image_folder.replace("\\","/")
list_folder = os.listdir(image_folder)
lists = []
for list in list_folder:
    lists.append(os.path.join(image_folder,list))
plt.figure(figsize=(6,6))
plt.imshow(matplotlib_tool.image_avg(lists))
plt.title("Averaging Image")
plt.show()