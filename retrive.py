
import csv
import cv2
import numpy as np

# retrieve compressed array from json file
import json

# Open the JSON file
with open('compressed.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Retrieve the compressed image from the data object
compressed_image = data


# retriving original array from compressed array
original_image = []
for i in compressed_image:
    
    curr = []
    for j in i:
        temp = [j[0] for k in range(j[1])]
        curr.extend(temp)
    original_image.append(curr)


# generate image from original image array

array = original_image

# convert the array into a binary image
binary_image = np.uint8(array)

# display the binary image
cv2.imshow("Retrieved image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


