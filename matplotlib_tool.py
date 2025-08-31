from PIL import Image
import matplotlib.pyplot as plt
def OpenImage(image_path):
    image = Image.open(image_path)
    plt.show(image)