# Import library, module
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import imagemodule

# List all images in folder
folder_path = input("Folder path: ").replace("\\","/")
folder_list = os.listdir(folder_path)
list = []
for i in folder_list:
    list.append(os.path.join(folder_path,i))
# Step 1: Call average image func and show it
plt.figure(num="Average Image",figsize=(5,5))
average_image = imagemodule.average_image(list)
plt.imshow(average_image)
plt.title("Average Image")
plt.show()
# Step 2: Call save_average_image func
new_image,new_name = imagemodule.save_average_image(folder_path,list) # Func save_average_image return 2 values
print("Save image successfully")
# Step 3: CDF_Image
image = Image.open(os.path.join(folder_path,new_name)).convert("L") # Convert RGB -> gray
image_array = np.array(image)
image_equalized = imagemodule.cdf_image(folder_path,new_name) # Call CDF func
image_equalized_array = np.array(image_equalized)
plt.figure(figsize=(12,12))
plt.subplot(2,2,1) # Make original image view
plt.imshow(image,cmap="gray")
plt.title("Original image")
plt.subplot(2,2,2) # Make histogram of original image view
plt.hist(image_array.flatten(),bins=256)
plt.title("Histogram of original image")
plt.subplot(2,2,3) # Make CDF's image view
plt.imshow(image_equalized,cmap="gray")
plt.title("CDF's image")
plt.subplot(2,2,4) # Make histogram of CDF's image view
plt.hist(image_equalized_array.flatten(),bins=256)
plt.title("Histogram of CDF's image")
plt.show()
# Step 4: Reverted image
reverted_image = imagemodule.revert_image(image_equalized_array) # Call reverted image func
fig,axs = plt.subplots(1,2,figsize=(10,5)) # Show result
fig.subplots_adjust(wspace=0.2,hspace=0.2)
axs[0].imshow(image_equalized,cmap="gray")
axs[0].set_title("Original image")
axs[1].imshow(reverted_image,cmap="gray")
axs[1].set_title("Reverted image")
plt.show()