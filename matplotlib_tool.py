from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
"""
# Func 1: Can bang anh xam
def histogram_equalization(image_path):
    image = Image.open(image_path)
    # Chuyen sang anh xam
    if image.mode != "L":
        image = image.convert("L")
    # Numpy array & histogram
    image_array = np.array(image)
    # Phan phoi tich luy CDF - Can bang anh xam
    histogram,bins = np.histogram(image_array,bins=256,range=(0,256),density=True)
    cdf = histogram.cumsum()
    cdf = 255*cdf/cdf[-1]
    image_equal = np.interp(image_array,bins[:-1],cdf)
    image_equalized = Image.fromarray(image_equal.astype("uint8"))
    # Tra ve anh da can bang xam
    return image_equalized
"""

# Func 2: Tinh trung binh anh
def image_avg(lists):
    # Tao mang ban dau
    total_array = np.array(Image.open(lists[0]),"f")
    count = 1
    # Tinh trung binh mang
    for list in lists[1:]:
        total_array += np.array(Image.open(list),"f")
        count += 1
    image_array = total_array/count
    # Tao anh tu mang trung binh
    image_average = Image.fromarray(image_array.astype("uint8"))
    # Tra ve dau ra
    return image_average