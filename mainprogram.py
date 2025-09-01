from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image_path = input("Image path: ")
image = Image.open(image_path)
grayscale_image = image.convert("L")
#plt.imshow(grayscale_image,cmap="gray")
image_array = np.array(grayscale_image)
plt.figure(num="figure 1",figsize=(8,6),facecolor="palegoldenrod")
plt.hist(image_array.flatten(),bins=128)
plt.title("LUOC DO ANH XAM")
plt.xlabel("Gia tri pixel")
plt.ylabel("So luong")
plt.show()