import re
region = input("Region crop(a,b,x,y): ")
list_region = re.findall(r'\d+',region)
crop_region = tuple([int(i) for i in list_region])
print(crop_region)