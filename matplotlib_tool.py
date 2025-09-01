from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
def OpenImage(image_path):
    image = Image.open(image_path)
    plt.imshow(image)
    plt.show()